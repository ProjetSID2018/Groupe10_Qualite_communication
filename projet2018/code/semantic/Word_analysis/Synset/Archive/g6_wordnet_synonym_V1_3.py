"""
Created on Wen Jan 10 22:33:30 2018
Groupe 6
@authors:C.H.,R.S.,J.E.
"""
# It's a programm that find many synonyms of a specific word with three
# way : the function wordnet in the package nltk, a translation french-english
# to find the synonyms and remade a translation of these in french and for the
# last way we used two synonyms websites named 'synonymo' and 'cnrtl'
# to found the synonyms.

import nltk.corpus
# We used the package pydeepl for the translation
import pydeepl
import itertools
import urllib.request
# We used the package bs4 to get the synonyms in the
# websites cnrtl and synonymo
import bs4


"""input : We give a word on input
output : We have a list on output
The function give us a list of synonyms for a specific word
with the wordnet method"""


def synonym(word):
    return [synset.lemma_names('fra')
            for synset in nltk.corpus.wordnet.synsets(word, lang='fra')][1]


"""input : We give a list on input
output : we have a list on output
The function give us a list of synonyms whithout the compounds words of our
input synonym list"""


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


"""input : We give a list, a boolean and two languages on input
output : we have a list on output
The function give us the translation of all words in the list from the first
language(FR) to the second language(EN) and print them if the boolean is true.
We used Deepl, the best translator online currently, to made this function"""


def traduction_x_to_y(text, display=False,
                      from_language='FR', to_language='EN'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if display:
        print(translation)
    return translation


"""input : We give a list, a boolean and two languages on input
output : we have a list on output
The function give us the translation of all words in the list from the first
language(EN) to the second language(FR) and print them if the boolean is true.
We used Deepl, the best translator online currently, to made this function"""


def traduction_y_to_x(text, display=False,
                      from_language='EN', to_language='FR'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if display:
        print(translation)
    return translation


"""input : We give a list and a string
output : we have a list on output
The function give us a list whithout the words that appears more than one time
on the list and also whithout the word which we search the synonyms """


def remove_repeat_words(syno, search_word):
    length = len(syno)
    i = 0
    while (i < length):
        while (syno[i].lower() == search_word):
                del syno[i]
                length = len(syno)
        word = syno[i].lower()
        j = i+1
        while (j < length):
            if (syno[j].lower == word):
                del syno[j]
                length = len(syno)
            else:
                j += 1
        i += 1


# Tests programms
if __name__ == '__main__':
    # Creation of the synonym list with the wordnet method
    word = 'chanteur'
    test = synonym(word)
    remove_compounds_words(test)
    print(test)


# Creation of the synonym list with the translation method
translate = traduction_x_to_y(word, display=True)
synonyms = nltk.corpus.wordnet.synsets(translate)
lemmas = set(itertools.chain.from_iterable
             ([word.lemma_names() for word in synonyms]))
lemma = list(lemmas)

for i in range(0, len(lemma)):
    translate = traduction_y_to_x(lemma[i], display=True)
    lemma[i] = translate

print(lemma)

# Creation of the synonym list with  two synonym websites
mm = 100
syno1 = []

opener = urllib.request.FancyURLopener({})
url = "http://www.cnrtl.fr/synonymie/" + word
f = opener.open(url)

content = f.read()

soup = bs4.BeautifulSoup(content, 'lxml')

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

soup = bs4.BeautifulSoup(content, 'lxml')

print('***********************')

i = 0
for p in soup.find_all(name='a', attrs={'word'}):
    i += 1
    # print(p.get_text())
    syno2.append(p.get_text())
    if i > mm:
        break


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
