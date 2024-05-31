#!/usr/bin/node
/* task 8
JavaScript script that fetches from
`https://fourtonfish.com/hellosalut/?lang=fr`
and displays the value of `hello` from that fetch
in the HTML element with id `hello`.

- The translation of “hello” must be displayed
in the HTML element with id `hello`
- Your script must work when it is
imported from the `<head>` tag
*/

document.addEventListener('DOMContentLoaded', () => {
  fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
    const helloContent = document.getElementById('hello');
    helloContent.textContent = data.hello;
  });
})
