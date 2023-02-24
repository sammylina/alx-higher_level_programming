$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (people, txtStatus) {
  $('DIV#character').text(people.name);
});
