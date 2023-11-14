#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    let y = 0;
    let widthPrint = '';
    while (x < this.width) {
      widthPrint = widthPrint + 'X';
      x++;
    }
    while (y < this.height) {
      console.log(widthPrint);
      y++;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}

module.exports = Rectangle;
