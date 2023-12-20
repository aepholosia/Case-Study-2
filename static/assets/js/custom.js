// custom.js

document.addEventListener('DOMContentLoaded', function () {
    const classificationLink = document.getElementById('classification-link');
    const regressionLink = document.getElementById('regression-link');
    const servicesContent = document.getElementById('services-content');
  
    classificationLink.addEventListener('click', function (event) {
      event.preventDefault();
  
      // You can load content dynamically here using AJAX or other methods
      // For simplicity, let's update the content with a sample message
      servicesContent.innerHTML = '<p>This is the dynamic content for Classification.</p>';
  
      // Hide the links after clicking
      classificationLink.classList.add('hidden-link');
      regressionLink.classList.add('hidden-link');
    });
  
    regressionLink.addEventListener('click', function (event) {
      event.preventDefault();
  
      // You can load content dynamically here using AJAX or other methods
      // For simplicity, let's update the content with a sample message
      servicesContent.innerHTML = '<p>This is the dynamic content for Regression.</p>';
  
      // Hide the links after clicking
      classificationLink.classList.add('hidden-link');
      regressionLink.classList.add('hidden-link');
    });
  });
  