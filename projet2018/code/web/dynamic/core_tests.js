var words = [{
    text: "Lorem",
    weight: 13
  }, {
    text: "Ipsum",
    weight: 10.5
  }, {
    text: "Dolor",
    weight: 9.4
  }, {
    text: "Sit",
    weight: 8
  }, {
    text: "Amet",
    weight: 6.2
  }, {
    text: "Consectetur",
    weight: 5
  }, {
    text: "Adipiscing",
    weight: 5
  }];

var words2 = [{
    text: "Lalala",
    weight: 13
  }, {
    text: "Iota",
    weight: 10.5
  }, {
    text: "Douleur",
    weight: 9.4
  }, {
    text: "Site",
    weight: 8
  }, {
    text: "Biere",
    weight: 6.2
  }, {
    text: "Insecte",
    weight: 5
  }, {
    text: "Apiculteur",
    weight: 5
  }];

var words3 = [{
    text: "Mouton",
    weight: 13
  }, {
    text: "Koala",
    weight: 10.5
  }, {
    text: "Bonheur",
    weight: 9.4
  }, {
    text: "Siege",
    weight: 8
  }, {
    text: "Bonbon",
    weight: 6.2
  }, {
    text: "Jamais",
    weight: 5
  }, {
    text: "Peinture",
    weight: 5
  }];

$(document).ready(function($) {
  var some_words_with_same_weight =
    $("#world_cloud_div_theme").jQCloud(words, {
      width: 500,
      height: 350,
      border: 1
    });
  $("#most_treated_word_article_theme").hide(10);
  $("#3_main_words_article_theme").hide(10);
});

$( ".radio" ).click(function() {
  $("#most_treated_theme_article_theme").hide();
  var id_selected = $(this).attr('id');
  if (id_selected == "_international") {
    var words_var = words;
  } else if (id_selected == "_france") {
    var words_var = words2;
  } else {
    var words_var = words3;
  }
  $('#world_cloud_div_theme').jQCloud('update', words_var, {
      width: 1000,
      height: 350
  });
  $("#most_treated_word_article_theme").show();
  $("#3_main_words_article_theme").show();
});