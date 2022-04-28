#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach(item => {
    if (item === searchElement) {
      occ++;
    }
  });
  return occ;
};
