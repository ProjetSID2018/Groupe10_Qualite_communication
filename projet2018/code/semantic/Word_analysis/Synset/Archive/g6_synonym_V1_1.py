# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:38:22 2018

@author: Admin
"""
# Groupe 6 CH,RS,JE
# FR : pour les synonymes
# EN : It's a programm that find the synonyms of a specific word
from nltk.corpus import wordnet as wn
import pydeepl  # traduction
from itertools import chain
from textblob import Word
import urllib.request
from bs4 import BeautifulSoup


# FR : On donne un mot et la fonction synonyme nous renvoie tout synonymes
# de ce mot
# EN : We give a word and the synonyme function send us all the synonyms
# of this word
def synonyme(word):
    return [synset.lemma_names('fra')
            for synset in wn.synsets(word, lang='fra')][1]


if __name__ == '__main__':
    word = "chien"
    test = synonyme(word)
    for i in range(0, len(test)):
        for j in range(0, len(test[i])-1):
            if (test[i][j] == '_' or test[i][j] == '-'):
                del test[i]
    print(test)


# FR : traduit de français à l'anglais à l'aide de Deepl
# le meilleur traducteur en ligne actuel
# EN : Translate from the french to english with Deepl
def traduction_x_to_y(text, affichage=False,
                      from_language='FR', to_language='EN'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if affichage:
        print(translation)
    return translation


# traduit de l'anglais au français à l'aide de Deepl
# le meilleur traducteur en ligne actuel
def traduction_y_to_x(text, affichage=False,
                      from_language='EN', to_language='FR'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if affichage:
        print(translation)
    return translation


translate = traduction_x_to_y("chien", affichage=True)
synonyms = wn.synsets(translate)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
lemma = list(lemmas)

for i in range(0, len(lemma)):
    translate = traduction_y_to_x(lemma[i], affichage=True)
    lemma[i] = translate

print(lemma)
# print(vb.synonym('bonjour', source_lang='fra', dest_lang='fra'))

name = "chien"
mm = 10

opener = urllib.request.FancyURLopener({})
url = "http://www.cnrtl.fr/synonymie/" + name
f = opener.open(url)

content = f.read()

soup = BeautifulSoup(content, 'lxml')

print('results for \"' + name + "\"")

print('***********************')

i = 0
for p in soup.find_all(name='td', attrs={'syno_format'}):
    i += 1
    print(p.get_text())
    if i > mm:
        break

opener = urllib.request.FancyURLopener({})
url = "https://www.synonymo.fr/syno/" + name
f = opener.open(url)

content = f.read()

soup = BeautifulSoup(content, 'lxml')

print('***********************')

i = 0
for p in soup.find_all(name='a', attrs={'word'}):
    i += 1
    print(p.get_text())
    if i > mm:
        break


sentences = " je suis un chien"
model = Word2Vec(sentences)


#  FR : Association des différentes listes obtenues grâce aux traductions
complete_translate = test + lemma
print(complete_translate)



# generer
# corpus wikipedia
# generer vecteuur mot
# matcher vecteur plus les mots sont proches pus ils sont sementiquement
#
# approche
# word to vek : word imbeding
# glof google
# jencine


# probléme des nom propres

# a faire : associer les synonymes aux mots
