#!/usr/bin/node

const req = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

req(url, (err, data) => {
  if (!err) console.log(JSON.parse(data.body).title);
});
