google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);



function drawBasic() {

	var json=[
		{"source": "figaro","nombre" : 210},
		{"source": "monde","nombre": 2015},
		{"source": "depeche","nombre" : 50},
		{"source": "libération","nombre": 45},
		{"source": "nouvel Obs","nombre" : 544},
		{"source": "Telerama","nombre": 45},
		{"source": "Futurasciences","nombre" : 76},
		{"source": "L’Humanité","nombre": 71}
	]

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'source');
	data.addColumn('number', "nombre");

	for (var i = 0; i <json.length; i++) {
	data.addRow([json[i].source,json[i].nombre ]);
	}

	var chart = new google.visualization.ColumnChart(
	document.getElementById('chart2_div_research'));
	chart.draw(data,{legend: {position: 'none'}});
}



$(window).resize(function(){ //make the graphics responsive
  drawBasic();
});
