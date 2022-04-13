#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

const f1 = fs.readFileSync(file1.toString(), 'utf-8');
const f2 = fs.readFileSync(file2.toString(), 'utf-8');

const f3 = f1.concat(f2);

fs.writeFile(file3, f3, function (err) {
  if (err) {
    throw err;
  }
});
