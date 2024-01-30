#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body);
      const wedgeAntillesMovies = filmsData.results.filter(movie =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(wedgeAntillesMovies.length);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
