# -*- coding: utf-8 -*-
"""============================================================================
Created on Tue Jan  10 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Cedric, Paul, Adrien

Main Program
============================================================================"""

# Server
from functions.g5_import_json import import_daily_jsons
from functions.g5_import_json import write_filtering_jsons
from functions.g5_integration import make_dict_filtering
import pickle

"""============================================================================
    links
============================================================================"""

# LINK ON THE SERVER
path_source = '/var/www/html/projet2018/data/clean/robot'
path_target = '/var/www/html/projet2018/data/clean/filtering'
stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/functions/stopwords.p', 'rb'))

# LINK ON GITHUB
#path_source = '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/Data/source_press_article'
#path_target = '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/Data/target_press_article'
#stop_words = pickle.load(open('/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/functions/stopwords.p', 'rb'))

# Import Jsons
articles = import_daily_jsons(path_source)


# articles = articles['artlibe42272018-01-08','artlibe19572018-01-08','artlibe25602018-01-08','artlibe32622018-01-08','','','','','','','','','','','','','','','','','','','','','','']
# Treatment
dict_filtering = make_dict_filtering(articles)

# Writing
write_filtering_jsons(dict_filtering, path_target)
