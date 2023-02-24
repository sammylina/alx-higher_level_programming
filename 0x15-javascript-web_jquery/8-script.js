$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (films, txtStatus) {
  const listContainer = $('UL#list_movies');
  films.results.forEach(film => {
    const list = $('<li></li>').text(film.title);
    listContainer.append(list);
  });
});
