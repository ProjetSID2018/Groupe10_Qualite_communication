 // Fonction JQUERY pour gérer la barre de navigation
(function($){
   // Quand le document est chargé
   $(document).ready(
    function(){
      var offset= $("header").offset().top;
      $(document).scroll(function(){
          var scrollTop = $(document).scrollTop();
          if(scrollTop > offset){
            $("nav").addClass("navbar-fixed-top");
          }
          else {
            $("nav").removeClass("navbar-fixed-top");
          }
      });

      var title = $("title").attr("id");
      if(title == "Search_Page"){
        $("#themeBar").hide();
      }
      else if(title == "theme_page"){
        $("#searchBar").hide();
      }
      else if(title == "index"){
        $("#searchBar").hide();
        $("#themeBar").hide();
      };
   });
})(jQuery);


      
    

