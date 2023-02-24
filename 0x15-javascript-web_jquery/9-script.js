$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (res, txtStatus) {
  $('DIV#hello').text(res.hello);
});
