// var val_most_treated_themes = [
//             ['Theme',           'Effectif'],
//             ['Art et Culture',    31090763],
//             ['Economie',          61801570],
//             ['Science',           73137148],
//             ['Sports',            74856000],
//             ['France',            79716203],
//             ['International',     81902307],
//             ['Santé',            141850000]
//           ];

// var words_associated_trend_1 = [
//   ["Mots liés au thème",  "Tendance"],
//   ["Verbe", "Tendance1"],
//   ["Nom", "Tendance2"],
//   ["Adjectif", "Tendance3"]
// ];
// 
// var words_associated_trend_2 = [
//   ["Mots liés au thème",  "Tendance"],
//   ["Word1", "Res1"],
//   ["Word2", "Res2"],
//   ["Word3", "Res3"]
// ];
// 
// var words_associated_trend_3 = [
//   ["Mots liés au thème",  "Tendance"],
//   ["Expression1", "Analyse1"],
//   ["Expression2", "Analyse2"],
//   ["Expression3", "Analyse3"]
// ];
// 
// var json_table = {
//    '1': {
//        word_link: "Lorem",
//        trend : 13
//      },
//      '2':{
//        text: "Ipsum",
//        weight: 10.5
//      }
// }

function start() {
	request_number_article_theme();
	request_word_trend();
	request_word_cloud_theme();
	request_word_cloud();
}

function request_number_article_theme() {
	$.ajax({
		//url:'',
		//url:'http://localhost:5000/theme',
		url:'http://127.0.0.1:5000/theme',
		type: 'GET',
		dataType: 'json',
		success: draw_number_article_theme,
		error: ajax_failed,
	});
}

function request_word_trend() {
	$( ".radio" ).click(function() {
		var theme = $(this).attr('id');
		$.ajax({
			//url:'',
			//url:'http://localhost:5000/trend/'+theme,
			url:'http://127.0.0.1:5000/trend/'+theme,
			type: 'GET',
			dataType: 'json',
			success: draw_word_trend,
			error: ajax_failed,
		});
	});
}

function request_word_cloud_theme() {
	$( ".radio" ).click(function() {
		var theme = $(this).attr('id');
		$.ajax({
			//url:'',
			//url:'http://localhost:5000/cloud/'+theme,
			url:'http://127.0.0.1:5000/cloud/'+theme,
			type: 'GET',
			dataType: 'json',
			success: draw_word_cloud_trend,
			error: ajax_failed,
		});
	});
}

function draw_number_article_theme(data_json_most_treated_themes) {
	//$("#most_treated_word_article_theme").hide();
	//$("#world_cloud_div_theme").hide();
	$("#3_main_words_article_theme").hide();
	//$('#word_cloud_cover').hide();
	google.charts.load('visualization', '1', {packages: ['corechart']});
	google.charts.setOnLoadCallback(function(){
    	var tab = new Array(['Theme','Effectif']);
		for (var i = 1; i <=Object.keys(data_json_most_treated_themes).length; i++) {
			tab[i] = [data_json_most_treated_themes[i].theme,data_json_most_treated_themes[i].effectif];
		}
		var data = new google.visualization.arrayToDataTable(tab);
		var options = {   
        	hAxis : {
          	title : "Nombre d'articles",
          	minValue: 0
        	},
        	width: 600,
        	height: 400,
        	bar: {groupWidth: "95%"},
        	legend: { position: "none" },
		};
		var chart = new google.visualization.BarChart(document.getElementById("series_chart_theme"));
		chart.draw(data, options);
		$(window).resize(function(){
			chart.draw(data, options);
		});
	});
	$("#most_treated_theme_article_theme").show();
}


function draw_word_trend(data_json_trend_themes) {
	$("#most_treated_theme_article_theme").hide();
	google.charts.load('visualization', '1', {packages: ['table']});
	google.charts.setOnLoadCallback(function(){
    	var options = {
      		showRowNumber: true,
      		width: '100%',
      		height: '100%'
    	};
    	var tab = new Array(['Mots liés au thème',  'Tendance']);
		for (var i = 1; i <=Object.keys(data_json_trend_themes).length; i++) {
			tab[i] = [data_json_trend_themes[i].mot,data_json_trend_themes[i].tendance];
		}
    	var data = google.visualization.arrayToDataTable(tab);
    	var table = new google.visualization.Table(document.getElementById('table_div'));
    	table.draw(data);
	});
	$("#3_main_words_article_theme").show();
}

function draw_word_cloud_trend(some_words) {
	$("#most_treated_theme_article_theme").hide();
	var tab = [];
	for (var i = 1; i <Object.keys(some_words).length+1; i++) {
		tab = tab.concat(some_words[i]);
	}
	$(".world_cloud_div_theme").jQCloud(tab);
	$(document).ready(function() {
		//$(".world_cloud_div_theme").jQCloud('destroy');
		//$(".word_cloud_row_graph").jQCloud(tab);
		$(".world_cloud_div_theme").jQCloud('update', tab);
	});
	$('#most_treated_word_article_theme').show();
}


function ajax_failed() {
//     compt+=1;
//     if ( compt == 3){
//         alert('erreur')
//     };
	alert('erreur');
}