#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let line = '';
    for (let i = 0; i < this.size; i++) {
      if (c !== undefined) {
        line += c;
      } else {
        line += 'X';
      }
    }
    for (let j = 0; j < this.size; j++) {
      console.log(line);
    }
  }
}

module.exports = Square;
