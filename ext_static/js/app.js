$(document).ready(function(){
  var path = location.pathname;
  if(path == "/"){
    $("#home-link").addClass("active");
  } else if(path == "/news/"){
    $("#news-link").addClass("active");
  } else if(path == "/works/"){
    $("#works-link").addClass("active");
  }

});

