#!/usr/bin/node
// This script takes an API URL as an argument and computes
// the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
const completed = {};

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const data = JSON.parse(body);
  for (const task of data) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
