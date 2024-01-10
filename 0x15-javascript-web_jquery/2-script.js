$(document).ready(function () {
  // Select the DIV#red_header element using jQuery
  var redHeaderDiv = $('#red_header');

  // Attach a click event handler to the DIV#red_header element
  redHeaderDiv.click(function () {
    // Select the <header> element using jQuery
    var headerElement = $('header');

    // Check if the <header> element was found
    if (headerElement.length) {
      // If found, update the text color to red (#FF0000)
      headerElement.css('color', '#FF0000');
    }
  });
});
