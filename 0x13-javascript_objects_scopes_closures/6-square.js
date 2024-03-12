#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let line = '';
    for (let i = 0; i < this.width; i++) {
      if (c !== undefined) {
        line += c;
      } else {
        line += 'X';
      }
    }
    for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
}

module.exports = Square;
