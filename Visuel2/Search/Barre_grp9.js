document.body.insertAdjacentHTML("afterBegin",


  '<nav class="navbar navbar-default">'+ 

    '/*Navigation bar*/'+    

    '<div id = "navBar" class="container">'+
      '<div class="navbar-header">'+
        '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#codebrainery-toggle-nav" aria-expanded="false">'+
          '<span class="sr-only">Toggle navigation </span>'+
          '<span class="icon-bar">'+'</span>'+
           '<span class="icon-bar">'+'</span>'+
           '<span class="icon-bar">'+'</span>'+
        '</button>'+
      '<img src="https://raw.githubusercontent.com/ProjetSID2018/Groupe10_Qualite_communication/master/Logos/bleu1.png" class="navbar-brand">'+'</img>'+
      '</div>'+
      '<div class="collapse navbar-collapse" id="codebrainery-toggle-nav">'+
        '<ul class="nav navbar-nav navbar-right">'+
          '<li class="item">'+'<a class="a-nav" href="#">Accueil</a>'+'</li>'+
          '<li class="item">'+'<a class="a-nav" href="#">Thèmes</a>'+'</li>'+
          '<li class="item">'+'<a class="a-nav" href="#">Recherche</a>'+'</li>'+
        '</ul>'+
      '</div>'+
    '</div>'+

    '/*Research*/'+
    '<nav class="navbar-default">'+
      '<div class="container-fluid">'+
        '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">'+
          '<ul class="nav navbar-nav">'+
            '<li>'+

              '/*Button research*/'+
              '<form class="navbar-form" id="search" action="YOUR_FORM_ACTION_HERE">'+
                '<div class="form-group">'+
                  '<div class="input-group">'+
                    '<input type="text" class="form-control" aria-describedby="searchicon" placeholder="Search" id="searchBar_input_research">'+'<span class="input-group-addon" role="button" id="searchicon" onClick="this.form.submit();" >'+'<span class="glyphicon glyphicon-search">'+'</span>'+'</span>'+
                  '</div>'+
                '</div>'+
              '</form>'+
            '</li>'+
            
            '/*Starting date*/'+
            '<li class="dropdown navgation" id="startDate_input_research">'+
                '<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Date de début<span class="1">'+'</span>'+'</a>'+
                '<ul class="dropdown-menu">'+
                  '/*Mettre votre calendrier*/'+
               '</ul>'+
            '</li>'+

            '<li class="dropdown navgation">'+
              '<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">'+'<label >Date de fin</label>'+'<span>'+'</span>'+'</a>'+
              '<ul class="dropdown-menu">'+
                '/*Mettre votre calendrier*/'+
              '</ul>'+
            '</li>'+
          '</ul>'+    
        '</div>'+
      '</div>'+
    '</nav>'+
  '</nav>'+
'</body>'+
'</html>');
