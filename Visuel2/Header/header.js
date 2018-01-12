/*fonction servant a inserer le header dans l'ensemble des pages du site. Permet d'actualiser tous les headers en meme temps.*/
/*utilise le lien vers bootstrap de chaque page */

document.body.insertAdjacentHTML("afterBegin",
'<header>'+
    '<nav class="navbar navbar-default">'+     
      '<div id = "navBar" class="container">'+
        '<div class="navbar-header">'+
          '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#codebrainery-toggle-nav" aria-expanded="false">'+
           '<span class="sr-only">Toggle navigation </span>'+
           '<span class="icon-bar"></span>'+
           '<span class="icon-bar"></span>'+
           '<span class="icon-bar"></span>'+
         '</button>'+
         '<img src="https://raw.githubusercontent.com/ProjetSID2018/Groupe10_Qualite_communication/master/Logos/bleu1.png" class="navbar-brand"></img>'+
        '</div>'+
        '<div class="collapse navbar-collapse" id="codebrainery-toggle-nav">'+
         '<ul class="nav navbar-nav navbar-right">'+
           '<li class="item"><a class="a.a-nav" href="#">Accueil</a></li>'+
           '<li class="item"><a class="a.a-nav" href="#">Thèmes</a></li>'+
           '<li class="item"><a class="a.a-nav" href="#">Recherche</a></li>'+
         '</ul>'+
        '</div>'+
      '</div>'+
    '</nav>'+
  '</header>');