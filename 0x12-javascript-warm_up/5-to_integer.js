#!/usr/bin/node

const argc = process.argv
if (!isNaN(parseInt(argc[2])))
	console.log(parseInt(argc[2]))
else
	console.log('Not a number')
