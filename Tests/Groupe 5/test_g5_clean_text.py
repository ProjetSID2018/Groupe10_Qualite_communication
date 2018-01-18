# -*- coding: utf-8 -*-
"""============================================================================
Created on Tue Jan 16 2018
@group: Group 10 - Communication
@author: Aissa

Function : Test that the corresponding function remove all non-word non-digit character
============================================================================"""

from g5_clean_text import clean_symbols;
texte="Emmanuel Macron, né le 21 décembre 1977 à Amiens, est un homme d'État français. Il est président de la République française depuis le 14 mai 2017. Après des études en philosophie et en science politique à l'''université Paris-Nanterre, il est diplômé de l'ENA, dont il sort inspecteur des finances. En 2008, il rejoint la banque d'affaires Rothschild & Cie, dont il devient deux ans plus tard associé-gérant.Ancien membre du Parti socialiste, il est nommé, en 2012, secrétaire général adjoint au cabinet du président de la République, François Hollande, avec qui il a collaboré lors de sa campagne présidentielle.En 2014, alors qu'il reste inconnu du grand public, il devient ministre de l'Économie, de l'Industrie et du Numérique."
attendu="Emmanuel Macron né le 21 décembre 1977 à Amiens est un homme d État français. Il est président de la République française depuis le 14 mai 2017. Après des études en philosophie et en science politique à l université ParisNanterre il est diplômé de l ENA dont il sort inspecteur des finances. En 2008 il rejoint la banque d affaires Rothschild Cie dont il devient deux ans plus tard associégérant.Ancien membre du Parti socialiste il est nommé en 2012 secrétaire général adjoint au cabinet du président de la République François Hollande avec qui il a collaboré lors de sa campagne présidentielle.En 2014 alors qu il reste inconnu du grand public il devient ministre de l Économie de l Industrie et du Numérique."
def test_clean_symbols():
    res=clean_symbols(texte)
    assert res == attendu
    
test_clean_symbols()