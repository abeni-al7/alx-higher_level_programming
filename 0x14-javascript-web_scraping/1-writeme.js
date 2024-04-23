#!/usr/bin/node
// This script accepts a file path and some string to write to
// the file. It writes the  ontent of the string to the file
// or the error object.
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
