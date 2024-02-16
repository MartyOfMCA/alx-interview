#!/usr/bin/node
/*
 * Print all characters of a Star Wars movie using
 * the Star Wars API.
 *
 * The script accepts the movie ID. This is used
 * to find a movie and consequently print the
 * characters who played in that movie.
 */

const { argv } = require('process');
const request = require('request');
let url = '';

if (argv.length === 3) {
  url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    getCharacter(JSON.parse(body).characters, 0);
  });
}

function getCharacter (characterURLs, index) {
  if (index === characterURLs.length) {
    return;
  }

  request(characterURLs[index], (error, response, data) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(data).name);
    getCharacter(characterURLs, (index + 1));
  });
}
