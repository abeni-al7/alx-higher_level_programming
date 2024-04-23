#!/usr/bin/node
// This script takes an API url and prints the number of
// movies where the character "Wedge Antilles" is present
// with the characterID 18

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const data = JSON.parse(body).results;
  let count = 0;
  for (const movie of data) {
    for (const character of movie.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
