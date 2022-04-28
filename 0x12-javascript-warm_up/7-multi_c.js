#!/usr/bin/node

let arg = process.argv[2];

if (!arg) {
  console.log('Missing number of occurrences');
} else {
  arg = parseInt(arg);
  if (arg > 0) {
    while (arg) {
      console.log('C is fun');
      arg--;
    }
  }
}
