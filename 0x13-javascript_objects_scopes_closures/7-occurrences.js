#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrence = 0;
  list.forEach(elem => {
    if (elem === searchElement) {
      occurrence++;
    }
  });
  return occurrence;
};
