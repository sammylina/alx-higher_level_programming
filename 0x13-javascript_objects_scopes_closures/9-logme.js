#!/usr/bin/node

exports.logMe = (function () {
  let argCount = 0;
  return function (item) {
    console.log(`${argCount}: ${item}`);
    argCount++;
  };
})();
