#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let size = '';
      for (let j = 0; j < this.width; j++) {
        size += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const alternate = this.width;
    this.width = this.height;
    this.height = alternate;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;