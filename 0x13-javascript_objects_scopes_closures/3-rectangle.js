#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let hgt = this.height;
    while (hgt) {
      console.log('X'.repeat(this.width));
      hgt--;
    }
  }
}

module.exports = Rectangle;
