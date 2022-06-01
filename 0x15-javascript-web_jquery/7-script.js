$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (user) {
    $('DIV#character').text(user.name);
  });
});
