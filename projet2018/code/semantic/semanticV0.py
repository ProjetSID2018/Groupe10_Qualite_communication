import json
import os
import requests

file_source_filtering = "/var/www/html/projet2018/data/clean/filtering/"
file_target = "/var/www/html/projet2018/data/clean/semantic/"

data_filter = []
for f in os.listdir(file_source_filtering):
    with open(file_source_filtering+f,"r") as file:
        data_filter.append(json.load(file))

data1 = [{
    "Emmanuel Macron" : "nom",
    "Emmanuel Macron" : "personalite politique",
    "polarite" : "positif",
    "Mots associes" : "president"
}, {
    "Paris" : "nom",
    "Paris" : "lieu",
    "polarite" : "positif",
    "mots associes" : "France"
}]


i = 1
for mot in data1:
    file_art = file_target + "artJT"+ str(i) + "_semantic.json"
    with open(file_art, "w") as fic:
        json.dump(mot, fic)
    i += 1


