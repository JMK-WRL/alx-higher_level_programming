document.addEventListener('DOMContentLoaded', function () {
  // Select the <header> element using document.querySelector
  var headerElement = document.querySelector('header');

  // Check if the <header> element was found
  if (headerElement) {
    // If found, update the text color to red (#FF0000)
    headerElement.style.color = '#FF0000';
  }
});
