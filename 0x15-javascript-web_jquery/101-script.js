$(function () {
  const $list = $('UL.my_list');

  $('DIV#add_item').click(function () {
    $list.append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    console.log('running');
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $list.empty();
  });
});
