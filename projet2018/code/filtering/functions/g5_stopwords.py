"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Elise Benois, Clément BRANDAO, Paul LAFARIE

Function : Get list of stop-words
============================================================================"""
import spacy
import json
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


#json_data = open('./Data/source_press_article/2018-01-08/lemonde/artlmde12018-01-08_robot.json', encoding='utf8')
#data = json.load(json_data)
#json_data.close()
#
#articles = {}
#art = data['content']


# tokeniz with spacy
def tokeniz(article):
    doc = nlp(article)
    return doc


# b = tokeniz(art)


def rec_entity(article):
    i = 0
    Ent = {}
    for entity in article.ents:
        Ent[i] = [entity.text, entity.label_]
        i += 1
    return Ent

'''
# tf
def tf(b):
    a = []
    for i in range(len(b)):
        a.append(str(b[i]))
    unique, counts = np.unique(a, return_counts=True)
    dict_words = {}
    for uk, ct in zip(unique, counts):
        sum_words = np.sum(counts)
        dict_words[uk] = ct/sum_words
        continue
    return dict_words


# List of stop_words
def get_stopwords():
    # list of spacy stopwords
    list_stopwords = []
    for find_stopwords in b:
        if find_stopwords.is_stop:
            list_stopwords.extend([find_stopwords])
    for i in range(len(list_stopwords)):
        list_stopwords[i] = str(list_stopwords[i])
    stop_words = set(stopwords.words('french'))
    list_stopwords_other = []
    for i in stop_words:
        list_stopwords_other.append(i)
    for i in range(len(list_stopwords_other)):
        if list_stopwords_other[i] not in list_stopwords:
            np.unique(list_stopwords.append(list_stopwords_other[i]))
    return list_stopwords


#stop_words = get_stopwords()
#
#lettre = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f',
#          'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n']
#for i in lettre:
#    stop_words.append(i)
#
#stop_words = np.unique(stop_words)
'''