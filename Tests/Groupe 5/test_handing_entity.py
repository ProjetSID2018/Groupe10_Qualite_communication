#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:31:08 2018

@author: Aissa 
"""

from g5_named_entity import handing_entity;
from g5_POS import tokeniz;

def test_handing_entity(): 
    
    attenduEnt={};
    text = "Emmanuel Macron, né le 21 décembre 1977 à Amiens, est un homme d'État français"
    res=tokeniz(text)
    Ent,Ent_Und=handing_entity(res)
    attenduEnt={'Emmanuel Macron': [0, 15, 'PER'], 'Amiens': [42, 48, 'LOC'], 'État': [65, 69, 'ORG']}
    attenduEntUnd={'Emmanuel_Macron': 'PER', 'Amiens': 'LOC', 'État': 'ORG'}
    assert Ent == attenduEnt
    assert Ent_Und== attenduEntUnd
    

test_handing_entity()