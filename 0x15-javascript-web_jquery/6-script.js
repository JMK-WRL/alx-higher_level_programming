$(document).ready(function () {
  // Select the DIV#update_header element using jQuery
  var updateHeaderDiv = $('#update_header');

  // Attach a click event handler to the DIV#update_header element
  updateHeaderDiv.click(function () {
    // Select the <header> element using jQuery
    var headerElement = $('header');

    // Update the text of the <header> element to "New Header!!!"
    headerElement.text('New Header!!!');
  });
});
