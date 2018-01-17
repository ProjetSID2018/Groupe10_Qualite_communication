import os
import lxml.html as lh
import json
import datetime as date
from bs4 import BeautifulSoup
import requests
import g4_futurasciences_v1 as g4_fusc
import g4_liberation_V1 as g4_libe
import g4_lemonde_V1 as g4_lmde
import g4_ladepeche_V1 as g4_lade
import g4_20minutes_v1 as g4_min
import G4_humanite_v1 as g4_huma
import g4_lepoint_v1 as lepoint

target_file = "/var/www/html/projet2018/data/clean/robot/" + str(date.datetime.now().date()) +"/"

# target_file = "data/clean/robot/" + str(date.datetime.now().date()) +"/"

deb = date.datetime.now()

try:
    lepoint.recovery_new_articles_lpt(target_file)
    print("Le Point OK")
except:
    print("Erreur Le Point")
    pass

try:
    g4_fusc.recovery_new_articles_fusc(target_file)
    print("Futurascience OK")
except:
    print("Erreur Futurascience")
    pass
try:
    g4_libe.recuperation_info_libe(target_file)
    print("Liberation OK")
except:
    print("Erreur Liberation")
    pass

try:
    g4_lmde.recuperation_info_lmde(target_file)
    print("Le Monde OK")
except:
    print("Erreur Le Monde")
    pass

try:
    g4_lade.recovery_new_articles_ld(target_file)
    print("La Depeche OK")
except:
    print("Erreur La Depeche")
    pass

try:
    g4_min.add_articles(target_file)
    print("20 Minutes OK")
except:
    print("Erreur 20 Minutes")
    pass

try:
    g4_huma.recuperation_info_hmnt(target_file)
    print("L'Humanité OK")
except:
    print("Erreur L'Humanité")
    pass

delta = date.datetime.now() - deb
print(delta.total_seconds())