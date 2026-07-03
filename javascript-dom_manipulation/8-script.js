document.addEventListener('DOMContentLoaded', function () {
  const helloDiv = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    });
});
