#!/usr/bin/node

const req = require('request');

const userId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/people/' + userId;

req(url, (err, data) => {
  if (!err) {
    const films = JSON.parse(data.body).films;
    console.log(films.length);
  }
});
