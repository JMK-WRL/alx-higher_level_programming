#!/usr/bin/node

const SquareBase = require('./5-square');

class SquareWithCharPrint extends SquareBase {
	charPrint(c) {{
		if (c === undefined) {
			c = 'X';
		}

		for (let x = 0; x < this.size; x++) {
			console.log(c.repeat(this.size));
		}
	}
}
