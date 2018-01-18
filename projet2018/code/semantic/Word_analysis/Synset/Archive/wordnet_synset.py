# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:38:22 2018

@author: Admin
"""

from nltk.corpus import wordnet as wn # pour les synonymes 

def synonyme(word):
    return [synset.lemma_names('fra') for synset in wn.synsets(word,lang='fra')][1]
    
if __name__ == '__main__': 
    word = 'chien'
    test=synonyme(word)
    print(test)
    

#Nom propre  
    
from itertools import chain
from nltk.corpus import wordnet

text= 'Trump'
synonyms = wordnet.synsets(text)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
# probléme des nom propres



#a faire : associer les synonymes aux mots
