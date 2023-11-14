#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg, 10);
let i = 0;

if (!isNaN(x)) {
	for (i; i < x; i++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
