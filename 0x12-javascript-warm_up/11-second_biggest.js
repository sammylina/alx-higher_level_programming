#!/usr/bin/node

const nums = process.argv.slice(2).map(n => parseInt(n));

if (nums.length > 1) {
  let firstBig = nums[0];
  let secondBig = nums[0];

  nums.forEach(n => {
    if (n > firstBig) {
      secondBig = firstBig;
      firstBig = n;
    } else if (n > secondBig && n < firstBig) {
      secondBig = n;
    } else if (firstBig === secondBig) {
      secondBig = n;
    }
  });
  console.log(secondBig);
} else {
  console.log(0);
}
