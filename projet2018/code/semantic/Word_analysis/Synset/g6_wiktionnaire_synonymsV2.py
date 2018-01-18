# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:38:22 2018

@author: CH,RS,JE
# Groupe 6 
# pour les synonymes
"""

import re, requests, sys
from urllib.request import FancyURLopener as opener
from bs4 import BeautifulSoup as bSoup

url = "https://fr.wiktionary.org/wiki/"

def getSynonyms(word) :
    ret = []
    op = opener()
    content = op.open(url + word).read()
    soup = bSoup(content,'lxml')
    for e in soup.find_all('span', id = re.compile('Synonymes')) :
        lang = e.find_previous('h2')
        attrib = lang.findChildren()
        b = True
        for a in attrib :
            if a.has_attr('id') and a['id'] == 'Français' :
                b = False
        if b : break
        tmp = e.find_next('ul')
        tmp = tmp.get_text()
        tmp = tmp.split('\n')
        tmp = tmp[1:len(tmp)-1]
        print(tmp)


dat = getSynonyms("chien")
