#!/usr/bin/node
const size = process.argv[2];
const num = Number(size);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < num; i++) {
    line += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}
