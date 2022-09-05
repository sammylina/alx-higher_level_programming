#!/usr/bin/node

const num = parseInt(process.argv[2]);
function factorial (num) {
  const product = num;
  if (Number.isNaN(num) || num === 1) {
    return 1;
  } else {
    return product * factorial(num - 1);
  }
}

console.log(factorial(num));
