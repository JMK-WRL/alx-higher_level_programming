$(document).ready(function () {
  // Select the DIV#add_item element using jQuery
  var addItemDiv = $('#add_item');

  // Attach a click event handler to the DIV#add_item element
  addItemDiv.click(function () {
    // Select the UL.my_list element using jQuery
    var myList = $('ul.my_list');

    // Add a new <li> element to the UL.my_list
    myList.append('<li>Item</li>');
  });
});
