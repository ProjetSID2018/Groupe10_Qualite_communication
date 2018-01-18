# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:45:06 2018
Group 10
@author: christelle
"""
# -*- coding: utf-8 -*-
# Groupe 10 AS , CL


from wiki_search_v1_4 import wikipedia_search


def test_wiki_search_v1_4():
    entite = "mACRON"
    res = wikipedia_search(entite)
    attendu = "https://fr.wikipedia.org/wiki/" + entite
    assert res == str(attendu)


test_wiki_search_v1_4()
