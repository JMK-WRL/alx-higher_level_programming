#!/usr/bin/node

const Square = require('./5-square');

class Square extends square {
	constructor (size) {
		super(size, size);
	}

	charPrint (c) {
		if (c === undefined) {
			this.print();
		} else {
			let i = 0;
			while (j < this.width) {
				console.log(c.repeat(this.width));
				i++;
			}
		}
	}
}

module.exports = Square;
