
/*ajout du lien necessaire pour les logos (font-incone) du footer*/

document.head.insertAdjacentHTML("beforeend",'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">');

/*fonction servant a inserer un footer dans les pages web. Permet d'actualiser tous les footer en meme temps.*/
/*utilise le lien vers bootstrap de chaque page */

document.body.insertAdjacentHTML("beforeend",
'<footer id ="ft1">' +
  '<div class="top-bar">' +
    '<div class="container-fluid">' +
      '<div class="row">' +
        '<div class = "display center">' +
          '<a href="#" class="navbar-center">' +
              '<img class="ups" src="https://raw.githubusercontent.com/ProjetSID2018/Groupe10_Qualite_communication/master/Logos/Paul%20Sabatier%20SID.png" >' +
          '</a>' +
        '</div>' +
        '<div class="social">' +
          '<ul class="social-network social-circle">' +
            '<li><a href="https://www.facebook.com/Watch-News-160938714533244/" class="icoFacebook" title="Facebook"><i class="fa fa-facebook"></i></a></li>' +
            '<li><a href="https://twitter.com/WatchNewsFR?lang=fr" class="icoTwitter" title="Twitter"><i class="fa fa-twitter"></i></a></li>' +
            '<li><a href="" class="icoGoogle" title="Google +"><i class="fa fa-google-plus"></i></a></li>' +
            '<li><a href="https://github.com/ProjetSID2018" class="icoGithub" title="Github"><i class="fa fa-github"></i></a></li>' +
          '</ul>' +       
        '</div>' +
        '<div class="entreprise">WATCHNEWS</div>' +
        '<div class="citation">Ce site est conçu dans le cadre d’un projet d’étude universitaire. Il n’a pas de vocation commerciale et est consultable gratuitement. Pour toute information ou réclamation, vous pouvez nous contacter à l’adresse suivante : watchnewsapp@gmail.com</div>' +
      '</div>' +
    '</div>' +
  '</div>' +
'</footer>');