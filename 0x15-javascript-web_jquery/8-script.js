$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (response) {
    const films = response.results;
    const $list = $('UL#list_movies');
    films.forEach(film => {
      $list.append(`<li>${film.title}</li`);
    });
  });
});
