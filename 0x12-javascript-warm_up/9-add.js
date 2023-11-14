#!/usr/bin/node

function add(a, b) {
	return a + b;
}

const Int1 = parseInt(process.argv[2], 10);
const Int2 = parseInt(process.argv[3], 10);

const result = add(Int1, Int2);

console.log(result);
