$("#buttonResearch_input_research").click(function() {
    var valueSearchBar = $("#searchBar_input_research").val();
    var themeChoisi = $("#themeList_select_research").val();
    var sourceChoisie = $("#sourceList_input_research").val();
    var dateDebutChoisie = $("#startDate_input_research").val();
    var dateFinChoisie = $("#endDate_input_research").val();
    document.getElementById("titre1").innerHTML = recupererTitre1();
    document.getElementById("titre2").innerHTML = recupererTitre2();
    document.getElementById("titre3").innerHTML = recupererTitre3();
    alert(valueSearchBar);
    $.ajax({
       url:'http://localhost:5000/test',
       type: 'GET',
       dataType: 'json',
       success: drawBasic,
       error: ajax_failed,
    });
});

function recupererTitre1(){
  var valueSearchBar = $("#searchBar_input_research").val();
  var dateDebutChoisie = $("#startDate_input_research").val();
  var dateFinChoisie = $("#endDate_input_research").val();
  return "Graphe 1 : Evolution du nombre d'article utilisant " + valueSearchBar + " par semaine et par source  entre le " + dateDebutChoisie + " et le " + dateFinChoisie;
}

function recupererTitre2(){
  var valueSearchBar = $("#searchBar_input_research").val();
  var dateDebutChoisie = $("#startDate_input_research").val();
  var dateFinChoisie = $("#endDate_input_research").val();
  return "Graphe 2 : Nombre d'utilisation de " + valueSearchBar + " par source entre le " + dateDebutChoisie + " et le " + dateFinChoisie;
}

function recupererTitre3(){
  var valueSearchBar = $("#searchBar_input_research").val();
  var dateDebutChoisie = $("#startDate_input_research").val();
  var dateFinChoisie = $("#endDate_input_research").val();
  return "Graphe 3 : Nuage des mots les plus associés à " + valueSearchBar + " entre le " + dateDebutChoisie + " et le " + dateFinChoisie;
}