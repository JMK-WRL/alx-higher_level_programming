$(document).ready(function () {
  // Select the DIV#toggle_header element using jQuery
  var toggleHeaderDiv = $('#toggle_header');

  // Attach a click event handler to the DIV#toggle_header element
  toggleHeaderDiv.click(function () {
    // Select the <header> element using jQuery
    var headerElement = $('header');

    // Check if the <header> element was found
    if (headerElement.length) {
      // Toggle the class between "red" and "green"
      headerElement.toggleClass('red green');
    }
  });
});
