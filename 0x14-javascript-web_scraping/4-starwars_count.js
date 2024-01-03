#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a request to the Star Wars API and count movies with Wedge Antilles
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body);
    const wedgeAntillesMovies = filmsData.results.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    console.log(wedgeAntillesMovies.length);
  }
});
