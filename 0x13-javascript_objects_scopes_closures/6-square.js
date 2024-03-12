#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
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
