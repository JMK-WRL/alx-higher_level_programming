$(document).ready(function () {
  // Define the URL to fetch the character name
  var apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Make an AJAX request using jQuery
  $.ajax({
    url: apiUrl,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      // Select the DIV#character element using jQuery
      var characterDiv = $('#character');

      // Display the character name in the DIV#character
      characterDiv.text(data.name);
    },
    error: function (error) {
      console.error('Error fetching data:', error);
    }
  });
});
