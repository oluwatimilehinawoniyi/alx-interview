#!/usr/bin/node

const axios = require('axios');

async function getMovieCharacters (movieId) {
  return axios.get(`https://swapi.dev/api/films/${movieId}/`)
    .then(response => {
      return response.data.characters;
    })
    .catch(error => {
      console.error(`Failed to retrieve data for movie ${movieId}:`, error);
      return [];
    });
}

async function printMovieCharacters (movieId) {
  getMovieCharacters(movieId)
    .then(characters => {
      if (characters.length > 0) {
        characters.forEach(characterUrl => {
          axios.get(characterUrl)
            .then(response => {
              console.log(response.data.name);
            })
            .catch(error => {
              console.error(`Failed to retrieve character data for ${characterUrl}:`, error);
            });
        });
      } else {
          console.log('No characters found for this movie.');
      }
    });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

printMovieCharacters(movieId);
