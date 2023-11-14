#!/usr/bin/node

const args = process.argv.slice(2);

function findSecondLargest(args) {
	const integers = args.map(arg => parseInt(arg, 10));

	if (integers.length <= 1) {
		return 0;
	}

	const sortedIntegers = integers.sort((a, b) => b - a);
	return sortedIntegers[1];
}

console.log(findSecondLargest(args));
