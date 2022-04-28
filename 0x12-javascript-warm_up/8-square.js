#!/usr/bin/node

let arg = process.argv[2];

if (!arg || isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  arg = parseInt(arg);
  const size = arg;
  if (arg > 0) {
    while (arg) {
      console.log('X'.repeat(size));
      arg--;
    }
  }
}
