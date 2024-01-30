#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      // Function to get character names
      const getCharacterName = async (characterUrl) => {
        const characterResponse = await new Promise((resolve, reject) => {
          request(characterUrl, (err, res, body) => {
            if (err) reject(err);
            else resolve(JSON.parse(body).name);
          });
        });
        return characterResponse;
      };

      // Promise to fetch character names in order
      const characterNamesPromises = charactersUrls.map(getCharacterName);

      // Resolve promises and print character names
      Promise.all(characterNamesPromises)
        .then(characterNames => {
          characterNames.forEach(name => console.log(name));
        })
        .catch(err => console.error('Error fetching character names:', err));
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
