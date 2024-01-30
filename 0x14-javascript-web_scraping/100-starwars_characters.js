#!/usr/bin/node

const axios = require('axios');

async function getCharacterName(characterUrl) {
  try {
    const response = await axios.get(characterUrl);
    return response.data.name;
  } catch (error) {
    console.error(`Error fetching character data: ${error.message}`);
    return null;
  }
}

async function main() {
  const filmId = process.argv[2];
  const endPoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  
  try {
    const response = await axios.get(endPoint);
    const characters = response.data.characters;

    const characterNames = await Promise.all(characters.map(getCharacterName));

    characterNames.forEach(name => {
      if (name) {
        console.log(name);
      }
    });
  } catch (error) {
    console.error(`Error fetching film data: ${error.message}`);
  }
}

main();
