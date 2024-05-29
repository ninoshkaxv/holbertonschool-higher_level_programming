#!/usr/bin/node
/* task 3
 JavaScript script that toggles the class
 of the header element when the user clicks
 on the tag id toggle_header:

The header element must always have one class: red or green,
never both in the same time and never empty.
If the current class is red, when the user click on
id toggle_header element, the class must be updated to green;
and the reverse.
*/

const headColor = document.querySelector('header');

const setColor = document.querySelector('#toggle_header');
setColor.addEventListener('click', () => {
  if (headColor.classList.length === 0) {
    headColor.classList.add('green');
  } else if (headColor.classList.value.includes('green')) {
    headColor.classList.replace('green', 'red');
  } else if (headColor.classList.value.includes('red')) {
    headColor.classList.replace('red', 'green');
  }
});

