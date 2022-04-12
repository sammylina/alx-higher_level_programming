#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let hgt = this.height;
    while (hgt) {
      console.log(c.repeat(this.width));
      hgt--;
    }
  }
}

module.exports = Square;
