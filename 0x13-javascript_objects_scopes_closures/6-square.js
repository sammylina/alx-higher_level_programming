#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let i = this.height; i > 0; i--) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
