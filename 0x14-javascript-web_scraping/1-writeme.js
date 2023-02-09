#!/usr/bin/node

const fs = require('fs');

const [filepath, message] = process.argv.slice(2, 4);

fs.writeFile(filepath, message, { encoding: 'utf8', flag: 'w+' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
