import json
import requests
import os


file_source_filtering = "/var/www/html/projet2018/data/clean/filtering/"
file_source_semantic = "/var/www/html/projet2018/data/clean/semantic/"

dataFilter = []
for f in os.listdir(file_source_filtering):
    dataFilter.append(json.load(file_source_filtering+f))

dataSemantic = []
for f in os.listdir(file_source_semantic):
    dataSemantic.append(json.load(file_source_semantic+f))



"""
a completer
"""

data = {1 : "sport", 2 : "informatique"}



