#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (Number.isNaN(num)) {
  console.log(1);
} else {
  let product = 1;
  for (let i = 1; i <= num; i++) {
    product *= i;
  }
  console.log(product);
}
