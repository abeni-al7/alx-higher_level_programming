#!/usr/bin/node
// This script accepts a URL to send a GET request to and
// prints the status code of the response.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
