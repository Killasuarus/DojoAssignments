$(document).ready(function(){
  var actions = $('button').attr("src");
  $('button').hover(function(){
    $('#wrapper').css('background-color',actions)
  }, function(){
    $(this).css('background-color', 'white');
  });
});
