/*Boites des dates*/
// $(function(){
//   $("#startDate_input_research").DateTimePicker({
//       dateTimeFormat : "dd-MM-yyyy"
//   });
// });
// 
// $(function(){
//   $("#endDate_input_research").DateTimePicker({
//       dateTimeFormat : "dd-MM-yyyy"
//   });
// });

function verification(word,start,end){
  d1=formattedDate(start);
  d2=formattedDate(end);

  if (d1==false || d2==false){
    alert('date impossible,réessayez')
  }else{
    d1=new Date(d1)
    d2=new Date(d2)

    if (word=='' || isValidDate(start)== false || isValidDate(end)== false|| d2<d1){
      if (word==''){
        alert('Il faut absolument rentrer un mot')
      }else if (isValidDate(start)== false || isValidDate(end)== false){
        alert('Il faut absolument rentrer les 2 dates dans le bon format')
      }else{
        alert('Il faut absolument que la première date soit inférieur ou égale à la deuxième')      
      }
      return false
    }else{
      return true
    }
  }
}

function formattedDate(date) {
  var day="";var month="";var year="";
  if (date.substring(2,3)=='/' && date.substring(5,6)=='/'){day=date.substring(0,2); month=date.substring(3,5); year=date.substring(6,10)}
  if (date.substring(2,3)=='/' && date.substring(4,5)=='/'){day=date.substring(0,2); month=date.substring(3,4); year=date.substring(5,9)}
  if (date.substring(1,2)=='/' && date.substring(3,4)=='/'){day=date.substring(0,1); month=date.substring(2,3); year=date.substring(4,8)}
  if (day!="" && month!="" && year!=""){
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    if (day<=31 && month<=12){
      return `${month}/${day}/${year}`;
    }else{
      return false;
    }
  }else{
    return false
  }
}

function isValidDate(date){
   var matches = /^(\d{1,2})[-\/](\d{1,2})[-\/](\d{4})$/.exec(date);
   if (matches == null) return false;
}



/*Auto-completion*/
/*var countries = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: 'code/web/countries.json'
});

$('#prefetch .typeahead').typeahead(null, {
  name: 'countries',
  source: countries
});*/



/*Boutton de recherche*/
$("#buttonResearch_input_research").click(function() {
  var valueSearchBar = $("#searchBar_input_research").val();
  var themeChoisi = $("#themeList_select_research").val();
  var sourceChoisie = $("#sourceList_input_research").val();
  var frequenceChoisie = $("#freqList_input_research").val();
  var dateDebutChoisie = $("#startDate_input_research").val();
  var dateFinChoisie = $("#endDate_input_research").val();

  if (frequenceChoisie=='Traitement par semaine'){frequenceChoisie='semaine'}
  if (frequenceChoisie=='Traitement par mois'){frequenceChoisie='mois'}
  if (frequenceChoisie=='Traitement par annee'){frequenceChoisie='annee'}
  if (themeChoisi=='Tous les thèmes'){themeChoisi='all'}
  if (sourceChoisie=='Toutes les sources'){sourceChoisie='all'}

  if (verification(valueSearchBar,dateDebutChoisie,dateFinChoisie)==true){
  	var find = '/';
  	var re = new RegExp(find, 'g');
	var dateDebutChoisie_ajax = dateDebutChoisie.replace(re, "-");
	var dateFinChoisie_ajax = dateFinChoisie.replace(re, "-");
    document.getElementById("titre1").innerHTML = recupererTitre1(valueSearchBar,dateDebutChoisie,dateFinChoisie,frequenceChoisie);
    $.ajax({
      url:'http://localhost:5000/recherche1' + '/' + valueSearchBar + '/' + dateDebutChoisie_ajax + '/' + dateFinChoisie_ajax + '/' + frequenceChoisie + '/' + themeChoisi + '/' + sourceChoisie,
      type: 'GET',
      dataType: 'json',
      success: Graph1,
      error: ajax_failed,
    });
//     document.getElementById("titre2").innerHTML = recupererTitre2(valueSearchBar,dateDebutChoisie,dateFinChoisie,frequenceChoisie);
//     $.ajax({
//       url:'http://localhost:5000/test' + '/' + valueSearchBar + '/' + dateDebutChoisie + '/' + dateFinChoisie + '/' + frequenceChoisie + '/' + themeChoisi + '/' + sourceChoisie,
//       type: 'GET',
//       dataType: 'json',
//       success: Graph2,
//       error: ajax_failed,
//     });
//     document.getElementById("titre3").innerHTML = recupererTitre3(valueSearchBar,dateDebutChoisie,dateFinChoisie);
//     $.ajax({
//       url:'http://localhost:5000/test' + '/' + valueSearchBar + '/' + dateDebutChoisie + '/' + dateFinChoisie + '/' + frequenceChoisie + '/' + themeChoisi + '/' + sourceChoisie,
//       type: 'GET',
//       dataType: 'json',
//       success: Graph3,
//       error: ajax_failed,
//     });
//     document.getElementById("titre4").innerHTML = recupererTitre4(valueSearchBar,dateDebutChoisie,dateFinChoisie);
//     $.ajax({
//       url:'http://localhost:5000/test' + '/' + valueSearchBar + '/' + dateDebutChoisie + '/' + dateFinChoisie + '/' + frequenceChoisie + '/' + themeChoisi + '/' + sourceChoisie,
//       type: 'GET',
//       dataType: 'json',
//       success: Graph4,
//       error: ajax_failed,
//     });
//     document.getElementById("titre5").innerHTML = recupererTitre5(valueSearchBar,dateDebutChoisie,dateFinChoisie);
//     $.ajax({
//       url:'http://localhost:5000/test' + '/' + valueSearchBar + '/' + dateDebutChoisie + '/' + dateFinChoisie + '/' + frequenceChoisie + '/' + themeChoisi + '/' + sourceChoisie,
//       type: 'GET',
//       dataType: 'json',
//       success: Graph5,
//       error: ajax_failed,
//     });
//     document.getElementById("titre6").innerHTML = recupererTitre6(valueSearchBar,dateDebutChoisie,dateFinChoisie);
//     $.ajax({
//       url:'http://localhost:5000/test' + '/' + valueSearchBar + '/' + dateDebutChoisie + '/' + dateFinChoisie + '/' + frequenceChoisie + '/' + themeChoisi + '/' + sourceChoisie,
//       type: 'GET',
//       dataType: 'json',
//       success: Graph6,
//       error: ajax_failed,
//     });
  }
});



/*Création des titres*/
function recupererTitre1(word,start,end,frequence){  return "Graphe 1 : Evolution du nombre d'article utilisant " + word + " par "+ frequence + " et par source(s) selectionnée(s) entre le " + start + " et le " + end;}
function recupererTitre2(word,start,end,frequence){  return "Graphe 2 : Evolution du nombre d'article utilisant " + word + " par "+ frequence + "semaine et par thème(s) selectionné(s) entre le " + start + " et le " + end;}
function recupererTitre3(word,start,end){  return "Graphe 3 : Nombre d'utilisation de " + word + " par source(s) selectionnée(s) entre le " + start + " et le " + end;}
function recupererTitre4(word,start,end){  return "Graphe 4 : Nombre d'utilisation de " + word + " par thème(s) selectionné(s) entre le " + start + " et le " + end;}
function recupererTitre5(word,start,end){  return "Graphe 5 : Nuage des mots les plus associés à " + word + " par source(s) selectionnée(s) entre le " + start + " et le " + end;}
function recupererTitre6(word,start,end){  return "Graphe 6 : Nuage des mots les plus associés à " + word + " par thème(s) selectionné(s) entre le " + start + " et le " + end;}


/*Création des graphiques*/
function Graph1(json_graph1) {
  google.charts.load('visualization', '1', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
  	var tab = new Array(['Periode','Source','Nombre']);
	for (var i = 1; i <=Object.keys(json_graph1).length; i++) {
		tab[i] = [json_graph1[i].periode,json_graph1[i].source,json_graph1[i].nombre];
	}
    var data = new google.visualization.DataTable();    
    var week=tab[1][0];
    var col=0;
    data.addColumn('string', 'source');
    for (var g = 1; g <tab.length; g++) {
      if (tab[g][0]==week){
        data.addColumn('number', tab[g][1]); //add every distinct sources present in the Json into column
        col=col+1;
      }
    }
    for (var i = 1; i <=tab.length; i+=col) {
      var tab2 = [tab[i][0]];
      for (var j = 0; j < col; j++) { //create a table proportional to the number of sources selected
        tab2.splice(j+1, 0, tab[j+i][2]);
      }
      data.addRow(tab2); //add the table to generate the lines
    }   
    var options = {
      curveType: 'function',
      legend: { position: 'bottom' }};
    var chart = new google.visualization.LineChart(document.getElementById('chart1_div_research'));
    $("#chart1_div_research").show();
    chart.draw(data,options);
  }
  $(window).resize(function(){ //make the graphics responsive
    drawChart();
  });
}

// function Graph2() {
// 
//   $("#chart2_div_research").show();
// }
// 
// function Graph3(){
//   google.charts.load('current', {packages: ['corechart', 'bar']});
//   google.charts.setOnLoadCallback(drawBasic);
//   function drawBasic() {
//     var json=[
//       {"source": "figaro","nombre" : 210},
//       {"source": "monde","nombre": 2015},
//       {"source": "depeche","nombre" : 50},
//       {"source": "libération","nombre": 45},
//       {"source": "nouvel Obs","nombre" : 544},
//       {"source": "Telerama","nombre": 45},
//       {"source": "Futurasciences","nombre" : 76},
//       {"source": "L’Humanité","nombre": 71}
//     ]
//     var data = new google.visualization.DataTable();
//     data.addColumn('string', 'source');
//     data.addColumn('number', "nombre");
//     for (var i = 0; i <json.length; i++) {
//     data.addRow([json[i].source,json[i].nombre ]);
//     }
//     var chart = new google.visualization.ColumnChart(
//     document.getElementById('chart2_div_research'));
//     chart.draw(data,{legend: {position: 'none'}});
//   }
//   $(window).resize(function(){ //make the graphics responsive
//     drawBasic();
//   });
//   $("#chart3_div_research").show();
// }
// 
// function Graph4(){
//   $("#chart4_div_research").show();
// }
// 
// function Graph5(){
//   $("#chart5_div_research").show();
// }
// 
// function Graph6(){
//   $("#chart5_div_research").show();
// }
// 
// 
function ajax_failed() {
    alert('erreur');
}