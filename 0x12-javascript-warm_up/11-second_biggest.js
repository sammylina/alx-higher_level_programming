#!/usr/bin/node

function searchSecondBiggest (list) {
  let fb, sb;
  if (list[0] > list[1]) {
    fb = list[0];
    sb = list[1];
  } else {
    fb = list[1];
    sb = list[0];
  }

  for (let i = 2; i < list.length; i++) {
    if (list[i] > fb) {
      sb = fb;
      fb = list[i];
    } else if ((list[i]) > sb && (list[i] < fb)) {
      sb = list[i];
    }
  }
  return sb;
}

function main () {
  const argList = [];

  for (let i = 2; i < process.argv.length; i++) {
    argList.push(parseInt(process.argv[i]));
  }

  if (argList.length < 2) {
    console.log(0);
  } else {
    const secondBiggest = searchSecondBiggest(argList);
    console.log(secondBiggest);
  }
}

main();
