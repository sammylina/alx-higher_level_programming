#!/usr/bin/node

let arg = process.argv[2];

if (!arg) {
  console.log('Not a number');
} else {
  arg = parseInt(arg);
  console.log('My number: ' + arg);
}
