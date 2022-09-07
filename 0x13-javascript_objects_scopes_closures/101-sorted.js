#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
let userId;
for (const key in dict) {
  userId = dict[key];

  if (userId in newDict) {
    newDict[userId].push(key);
  } else {
    newDict[userId] = [key];
  }
}

console.log(newDict);
