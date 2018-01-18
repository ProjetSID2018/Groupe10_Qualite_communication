#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:07:38 2018
/home/formationsid/Documents/Projet_Interpromo/wikipedia
@author: formationsid
"""
import json

json_data = open('../../out.json')
data = json.load(json_data)

print("Entrer un mot")
line = input()

reference = {}
i = 0
while i < len(data):
    reference[data[i]['name']] = data[i]['url']
    i = i + 1

try :
    print(reference[line])
except :
    print("Page introuvable")