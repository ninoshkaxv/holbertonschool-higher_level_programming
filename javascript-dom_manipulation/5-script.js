#!/usr/bin/node
/* task 5
Write a JavaScript script that updates the text
of the header element to New Header!!!
when the user clicks on the element with id `update_header``
*/

const UpdateHeader = document.querySelector('header');

const setHeader = document.querySelector('#update_header');
setHeader.addEventListener('click', () => {
  UpdateHeader.textContent = 'New Header!!!';
});
