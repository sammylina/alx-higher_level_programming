#!/usr/bin/node

exports.esrever = function (list) {
  const reverseArr = [];
  let listLen = list.length;

  while (listLen) {
    reverseArr.push(list.pop());
    listLen = list.length;
  }
  return reverseArr;
};
