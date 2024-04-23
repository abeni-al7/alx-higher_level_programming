#!/usr/bin/node
// This script accepts a movie ID and returns the title of
// the StarWars movie where the episode number matches a
// given integer using the Star wars API with the endpoint
// https://swapi-api.alx-tools.com/api/films/:id

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
