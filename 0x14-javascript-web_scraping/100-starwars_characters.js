#!/usr/bin/node

const axios = require('axios');
const endPoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

axios.get(endPoint)
  .then(response => {
    if (response.status === 200) {
      const characters = response.data.characters;

      characters.forEach(character => {
        axios.get(character)
          .then(response => {
            if (response.status === 200) {
              console.log(response.data.name);
            }
          })
          .catch(err => {
            throw err;
          });
      });
    }
  })
  .catch(err => {
    throw err;
  });
