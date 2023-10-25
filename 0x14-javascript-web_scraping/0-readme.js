#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];

if (process.argv.length < 3) {
  console.error('Usage: node readfile.js <file_path>');
  process.exit(1);
}

fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
