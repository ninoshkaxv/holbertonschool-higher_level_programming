#!/usr/bin/node
/* task 6
Write a JavaScript script that fetches the character name
from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag with id character.
*/

const ActorName = document.querySelector('#character');

fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => { ActorName.textContent = data.name; });
