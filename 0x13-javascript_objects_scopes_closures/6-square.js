#!/usr/bin/node

const SquareBase = require('./5-square');

class SquareWithCharPrint extends SquareBase {
	charPrint(c0 {
		if (c === undefined) {
			c = 'X';
		}

		for (let i = 0; i < this.size; i++) {
			console.log(c.repeat(this.size));
		}
	}
}
