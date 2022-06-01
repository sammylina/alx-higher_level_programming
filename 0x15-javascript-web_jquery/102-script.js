$(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, function (res) {
      $('DIV#hello').text(res.hello);
    });
  });
});
