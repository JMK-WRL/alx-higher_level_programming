#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg, 10);
let i = 0;
let j = 0;

if (!isNaN(size)) {
	for (i; i < size; i++) {
		let row = '';
		for (j; j < size; j++) {
			row += 'X';
		}
		console.log(row);
	}
} else {
	console.log('Missing size');
}
