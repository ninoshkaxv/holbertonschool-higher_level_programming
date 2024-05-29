#!/usr/bin/node
/* task 2
  JavaScript script that adds the class red to the header element when the user clicks on the tag with id red_header
*/

const headColor = document.querySelector('header');

const setColor = document.querySelector('#red_header');
setColor.addEventListener('click', () => {
  headColor.classList.add('red');
});
