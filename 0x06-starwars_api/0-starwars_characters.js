#!/usr/bin/node

if ((process.argv).length > 2) {
  const movieId = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
  const request = require('request');

  request(url, (err, res, body) => {
    if (err) console.error(err);
    else if (res.statusCode === 200) {
      const charactersUrl = JSON.parse(body).characters;
      const characterRequests = charactersUrl.map(charUrl => {
        return new Promise((resolve, reject) => {
          request(charUrl, (error, response, bodyChar) => {
            if (error) reject(error);
            else if (response.statusCode === 200) resolve(JSON.parse(bodyChar).name);
            else reject(new Error(`Failed to fetch ${charUrl}`));
          });
        });
      });
      // console.log(characterRequests);
      Promise.all(characterRequests)
        .then(charNames => {
          charNames.forEach(name => console.log(name));
        })
        .catch(error => console.error(error));
    }
  });
}
