#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (first, second) {
  console.log(first + second);
}

add(first, second);
