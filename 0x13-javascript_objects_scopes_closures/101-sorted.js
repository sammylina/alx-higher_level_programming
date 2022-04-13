#!/usr/bin/node

const dict = require('./101-data').dict;

const store = {};

for (const key in dict) {
  if (store[dict[key]]) {
    store[dict[key]].push(key);
  } else {
    store[dict[key]] = [key];
  }
}

console.log(store);
