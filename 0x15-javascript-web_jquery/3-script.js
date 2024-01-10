$(document).ready(function () {
  // Select the DIV#red_header element using jQuery
  var redHeaderDiv = $('#red_header');

  // Attach a click event handler to the DIV#red_header element
  redHeaderDiv.click(function () {
    // Select the <header> element using jQuery
    var headerElement = $('header');

    // Check if the <header> element was found
    if (headerElement.length) {
      // If found, add the class "red" to the <header> element
      headerElement.addClass('red');
    }
  });
});
