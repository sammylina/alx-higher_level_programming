$(function () {
  const langInput = $('INPUT#language_code');

  function greet (lang) {
    const langCode = langInput.val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (res) {
      $('DIV#hello').text(res.hello);
    });
  }

  langInput.on('change', function () {
    greet(langInput.val());
  });

  $('INPUT#btn_translate').on('click', function () {
    greet(langInput.val());
  });
});
