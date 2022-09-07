#!/usr/bin/node

const fs = require('fs');
const [source1, source2, destination] = process.argv.slice(2);

const file1 = fs.readFileSync(source1, 'utf-8');
const file2 = fs.readFileSync(source2, 'utf-8');

fs.writeFileSync(destination, file1 + file2, 'utf-8');
