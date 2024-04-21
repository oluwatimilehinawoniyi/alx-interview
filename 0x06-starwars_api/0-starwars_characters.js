#!/usr/bin/node

const request = require('request');

const episodeNumber = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

request(url, async (error, response, body) => {
  if (!error) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    for (const character of characters) {
      const promise = new Promise((resolve, reject) => {
        request(character, (error, response, names) => {
          if (!error) {
            resolve(JSON.parse(names).name);
          } else {
            reject(error);
          }
        });
      });
      console.log(await promise);
    }
  }
});
