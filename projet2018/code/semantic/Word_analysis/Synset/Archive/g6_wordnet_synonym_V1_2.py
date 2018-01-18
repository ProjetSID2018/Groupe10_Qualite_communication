# Groupe 6 CH,RS,JE

# It's a programm that find many synonyms of a specific word with three
# way : the function wordnet in the package nltk, a translation french-english
# to find the synonyms and remade a translation of these in french and for the
# last way we used two synonyms websites named 'synonymo' and 'cnrtl'
# to found the synonyms.

from nltk.corpus import wordnet as wn
# We used the package pydeepl for the translation
import pydeepl
from itertools import chain
""" from textblob import Word"""
import urllib.request
from bs4 import BeautifulSoup


# EN : We give a word and the synonyme function send us all the synonyms
# of this word
def synonym(word):
    return [synset.lemma_names('fra')
            for synset in wn.synsets(word, lang='fra')][1]


# We remove all the compounds words of our synonym list.
def remove_compounds_words(syno):
    length = len(syno)
    i = 0
    while (i < length):
        is_composed = False
        for j in range(0, len(syno[i])):
            if (syno[i][j] == '_' or syno[i][j] == '-' or syno[i][j] == ' '):
                is_composed = True
        if is_composed:
            del syno[i]
            length = len(syno)
        else:
            i += 1


# Translate from french to english with Deepl the best translator
# online currently
def traduction_x_to_y(text, display=False,
                      from_language='FR', to_language='EN'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if display:
        print(translation)
    return translation


# Translate from english to french with Deepl the best translator
# online currently
def traduction_y_to_x(text, display=False,
                      from_language='EN', to_language='FR'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if display:
        print(translation)
    return translation


# We remove all the words that appears more than one time and we remove also
# the word which we search the synonyms
def remove_repeat_words(syno, search_word):
    length = len(syno)
    i = 0
    while (i < length):
        while (syno[i] == search_word):
                del syno[i]
                length = len(syno)
        word = syno[i]
        j = i+1
        while (j < length):
            if (syno[j] == word):
                del syno[j]
                length = len(syno)
            else:
                j += 1
        i += 1


# Tests programms
if __name__ == '__main__':
    # Creation of the synonym list with the wordnet method
    word = 'mort'
    test = synonym(word)
    remove_compounds_words(test)
    print(test)


# Creation of the synonym list with the translation method
translate = traduction_x_to_y(word, display=True)
synonyms = wn.synsets(translate)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
lemma = list(lemmas)

for i in range(0, len(lemma)):
    translate = traduction_y_to_x(lemma[i], display=True)
    lemma[i] = translate

"""print(lemma)
print(vb.synonym('bonjour', source_lang='fra', dest_lang='fra'))"""

# Creation of the synonym list with  two synonym websites
mm = 100
syno1 = []

opener = urllib.request.FancyURLopener({})
url = "http://www.cnrtl.fr/synonymie/" + word
f = opener.open(url)

content = f.read()

soup = BeautifulSoup(content, 'lxml')

print('results for \"' + word + "\"")

print('***********************')

i = 0
for p in soup.find_all(name='td', attrs={'syno_format'}):
    i += 1
    """print(p.get_text())"""
    syno1.append(p.get_text())
    if i > mm:
        break

# print(syno1)

syno2 = []
opener = urllib.request.FancyURLopener({})
url = "https://www.synonymo.fr/syno/" + word
f = opener.open(url)

content = f.read()

soup = BeautifulSoup(content, 'lxml')

print('***********************')

i = 0
for p in soup.find_all(name='a', attrs={'word'}):
    i += 1
    # print(p.get_text())
    syno2.append(p.get_text())
    if i > mm:
        break

""" enlever_mots_composes(syno1)"""


#  We associate the 3 synonyms list in one list
complete_translate = test + lemma + syno1
remove_compounds_words(complete_translate)
print(complete_translate)
remove_repeat_words(complete_translate, word)
print('***********************')
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
