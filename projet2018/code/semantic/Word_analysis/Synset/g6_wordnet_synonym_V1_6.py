"""
Created on Thu 11 8:30:00 2018
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
# import pydeepl
# import itertools
# import urllib.request
# We used the package bs4 to get the synonyms in the
# websites cnrtl and synonymo
# import bs4


"""input : We give a word on input
output : We have a list on output
The function give us a list of synonyms for a specific word
with the wordnet method"""


def synonym(word):
    try:
        return [synset.lemma_names('fra')
                for synset in nltk.corpus.wordnet.synsets(word, lang='fra')][1]
    except:
        return 'NA'


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


"""def translation_x_to_y(text, display=False,
                       from_language='FR', to_language='EN'):

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if display:
        print(translation)
    return translation"""


"""input : We give a list and a string
output : we have a list on output
The function give us a list whithout the words that appears more than one time
on the list and also whithout the word which we search the synonyms """


def remove_repeat_words(syno, search_word):
    syno2 = []
    for word in syno:
        if word not in syno2 and word != search_word:
            syno2.append(word)
    return syno2


""" input : we give a word on input
    output : we have a list on output
The function give us a list of synonyms with the translation method."""


"""def translate_method(word):
    translate = translation_x_to_y(word, display=False,
                                   from_language='FR', to_language='EN')
    synonyms = nltk.corpus.wordnet.synsets(translate)
    lemmas = set(itertools.chain.from_iterable
                 ([word.lemma_names() for word in synonyms]))
    lemma = list(lemmas)

    for i in range(0, len(lemma)):
        translate = translation_x_to_y(lemma[i], display=False,
                                       from_language='EN', to_language='FR')
        lemma[i] = translate
    return(lemma) """


""" input : we give a word, the number of synonyms and the website url on input
    output : we have a list on output
The function give us a certain number of synonyms of the word we give on input.
The number of synonyms is defined by the variable number_word. We give also the
synonym website url."""


"""def website_method(word, number_word, url):
    syno = []
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    soup = bs4.BeautifulSoup(content, 'lxml')
    i = 0
    for p in soup.find_all(name='td', attrs={'syno_format'}):
        i += 1
        syno.append(p.get_text())
        if i > number_word:
            break
    return(syno)"""

"""input : we give a word on input
output : we return a word on output
The function give us the first synonym of a specific word with the wordnet
method """


def give_the_first_wordnet_synonym(word):
    final_list = synonym(word)
    remove_compounds_words(final_list)
    final_list = remove_repeat_words(final_list, word)
    try:
        return (final_list[0])
    except:
        return 'NA'


"""input : we give a word which we want the synonyms on input
output : we returned a string on output
The function give us the first synonym of a specific word"""


"""def give_the_first_synonym(word):
    final_list = []
    try:
        final_list += website_method(word, 100,
                                     "http://www.cnrtl.fr/synonymie/" + word)
    except:
        print("This word has no synonym on the website cnrtl")
    try:
        final_list += translate_method(word)
    except:
        print("This word has no synonym with the translation method")
    try:
        final_list += synonym(word)
    except:
        print("This word has no synonym with the wordnet method")
    for i in range(0, len(final_list)):
        final_list[i] = final_list[i].lower()
    remove_compounds_words(final_list)
    final_list = remove_repeat_words(final_list, word)
    try:
        return (final_list[0])
    except:
        return 'NA'"""


# Tests programms
if __name__ == '__main__':
    # MAIN TEST of the synonym function with the combination
    # of synonyms methods
    """ word = 'kapla'
    synonyme = give_the_first_synonym(word)
    print('Le synonyme est ', synonyme)"""

    # Test of the function give_the_first_synonym(word)
    word = 'chien'
    print(give_the_first_wordnet_synonym(word))

    # Creation of the synonym list with  another synonym website
    """
    syno2 = []
    opener = urllib.request.FancyURLopener({})
    url = "https://www.synonymo.fr/syno/" + word
    f = opener.open(url)

    content = f.read()

    soup = bs4.BeautifulSoup(content, 'lxml')
    i = 0
    for p in soup.find_all(name='a', attrs={'word'}):
        i += 1
        syno2.append(p.get_text())
        if i > mm:
            break
    """
