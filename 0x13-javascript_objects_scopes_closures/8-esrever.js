#!/usr/bin/node

exports.esrever = function (list) {
  let temp;
  let leftidx = 0;
  let rightidx = list.length - 1;

  while (leftidx < rightidx) {
    temp = list[leftidx];
    list[leftidx] = list[rightidx];
    list[rightidx] = temp;

    leftidx++;
    rightidx--;
  }
  return list;
};
