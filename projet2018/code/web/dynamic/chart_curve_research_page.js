google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);



function drawChart() {

  var json  = [
    {"week": "w1", "source":"La Dépêche", "nombre": 10 },
    {"week": "w1", "source":"Le Figaro", "nombre": 1 },
    {"week": "w1", "source":"Le Point", "nombre": 12 },
    {"week": "w1", "source":"Le Monde", "nombre": 2 },
    {"week": "w1", "source":"Libération", "nombre": 9 },
    {"week": "w1", "source":"Nouvelle Obs", "nombre": 13 },
    {"week": "w1", "source":"Telerama", "nombre": 6 },
    {"week": "w1", "source":"Futurasciences", "nombre": 5 },
    {"week": "w1", "source":"L’Humanité", "nombre": 9 },
    {"week": "w2", "source":"La Dépêche", "nombre": 20 },
    {"week": "w2", "source":"Le Figaro", "nombre": 35 },
    {"week": "w2", "source":"Le Point", "nombre": 15 },
    {"week": "w2", "source":"Le Monde", "nombre": 17 },
    {"week": "w2", "source":"Libération", "nombre": 3 },
    {"week": "w2", "source":"Nouvelle Obs", "nombre": 22 },
    {"week": "w2", "source":"Telerama", "nombre": 8 },
    {"week": "w2", "source":"Futurasciences", "nombre": 3 },
    {"week": "w2", "source":"L’Humanité", "nombre": 6 },
    {"week": "w3", "source":"La Dépêche", "nombre": 15 },
    {"week": "w3", "source":"Le Figaro", "nombre": 5 },
    {"week": "w3", "source":"Le Point", "nombre": 11 },
    {"week": "w3", "source":"Le Monde", "nombre": 17 },
    {"week": "w3", "source":"Libération", "nombre": 7 },
    {"week": "w3", "source":"Nouvelle Obs", "nombre": 23 },
    {"week": "w3", "source":"Telerama", "nombre": 28 },
    {"week": "w3", "source":"Futurasciences", "nombre": 13 },
    {"week": "w3", "source":"L’Humanité", "nombre": 9 }
  ]

  var data = new google.visualization.DataTable();
  var w1=json[0].week;
  var col=0;

  data.addColumn('string', "week");
  for (var g = 0; g <json.length; g++) {
    if (json[g].week==w1){
      data.addColumn('number', json[g].source); //add every distinct sources present in the Json into column
      col=col+1;
    }
  }

  for (var i = 0; i <json.length; i+=col) {
    var tab = [json[i].week];
    for (var j = 0; j <col; j++) { //create a table proportional to the number of sources selected
      tab.splice(j+1,0,json[j+i].nombre); 
    }
    data.addRow(tab) //add the table to generate the lines
  }

  var options = {
    curveType: 'function',
    legend: { position: 'bottom' }};

  var chart = new google.visualization.LineChart(document.getElementById('chart1_div_research'));
  chart.draw(data,options);
}

$(window).resize(function(){ //make the graphics responsive
  drawChart();
});