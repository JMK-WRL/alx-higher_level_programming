$(document).ready(function () {
  // Define the URL to fetch the list of movies
  var apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Make an AJAX request using jQuery
  $.ajax({
    url: apiUrl,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      // Select the UL#list_movies element using jQuery
      var listMoviesUl = $('#list_movies');

      // Loop through each movie in the data and add its title to the list
      data.results.forEach(function (movie) {
        // Create a new list item element with the movie title
        var listItem = $('<li>').text(movie.title);

        // Append the list item to the UL#list_movies
        listMoviesUl.append(listItem);
      });
    },
    error: function (error) {
      console.error('Error fetching data:', error);
    }
  });
});
