#!/usr/bin/node
/* task 7
JavaScript script that fetches and
lists the `title` for all movies by using
this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- All movie titles must be list in the HTML
`ul` element with id `list_movies`
*/

const FilmList = document.querySelector('#list_movies');

fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    for (let index = 0; index < data.results.length; index++) {
      const NewFilm = document.createElement('li');
      NewFilm.textContent = data.results[index].title;
      FilmList.appendChild(NewFilm);
    }
  });
