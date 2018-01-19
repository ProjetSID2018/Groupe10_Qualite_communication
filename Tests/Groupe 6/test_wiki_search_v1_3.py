# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Groupe 10 AS , CL

from wiki_search_v1_3 import wikipedia_search


def test_wiki_search_v1_3():
    entite = "Macron"
    res = wikipedia_search(entite)
    attendu = "https://fr.wikipedia.org/wiki/" + entite
    assert res == str(attendu)


test_wiki_search_v1_3()
