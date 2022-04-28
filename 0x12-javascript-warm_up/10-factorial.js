#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 1) {
    return num;
  } else {
    return num * factorial(num - 1);
  }
}

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
