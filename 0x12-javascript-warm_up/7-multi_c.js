#!/usr/bin/node

const argc = process.argv[2];

if (!isNaN(argc)) {
  for (let i = 0; i < argc; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
