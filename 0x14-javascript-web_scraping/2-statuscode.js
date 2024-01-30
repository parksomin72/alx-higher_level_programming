#!/usr/bin/node

const request = require('request');

request({ url: process.argv[2], method: 'GET' }, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response && response.statusCode}`);
  }
});
