#!/usr/bin/node

const oldList = require('./100-data').list;

const newList = oldList.map((elem, idx) => (elem * idx));
console.log(oldList);
console.log(newList);
