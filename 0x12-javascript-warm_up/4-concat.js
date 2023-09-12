#!/usr/bin/node

const argc = process.argv;

if (argc[2] === '' && argc[3] === '') {
  argc[3] = 'undefined';
  argc[2] = 'undefined';
  console.log(`${argc[2]} is ${argc[3]}`);
}
if (argc[3] === '') {
  argc[3] = 'undefined';
  console.log(`${argc[2]} is ${argc[3]}`);
} else {
  console.log(`${argc[2]} is ${argc[3]}`);
}
