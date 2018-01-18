# Group 6 LAFONT Nicolas, QUESNOT Sandy, VAYSSE Robin
# Version 1.1 : initial version
# !/usr/bin/env python3
# -*- coding : utf-8 -*-

from difflib import SequenceMatcher
import string
import pandas as pd
import json
import nltk
import os
from nltk import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords

"""
Give a similarity rate between two strings
"""

"""
How Work SequenceMatcher function
Sequence matcher: Compares all characters between the two words
and counts the similarities.
Do the same thing again, taking the second word backwards and counting
it back similarities.

"""

"""
1- We drop stopwords
2- Calculate the similarities between serious words and article title
4- Define a score by article
5- Define a rule about this article

"""

"""
Elimination des mots vides
"""


def clean_title(json_data_link):
    stop_words = stopwords.words('french')

    stop_words.append('les')
    stop_words.append('«')
    stop_words.append('»')

    json_data = open(json_data_link)
    file = json.load(json_data)
    title = file["title"]
    title = title.replace("'", " ")
    return([i for i in word_tokenize(title.lower()) if i not in stop_words and
            i not in string.punctuation])


def serious_topic(clean_title):
    nb_serious_words = 0
    for s in serious_words['word']:
        for t in clean_title:
            if SequenceMatcher(None, s, t).ratio() > 0.9:
                nb_serious_words = nb_serious_words + 1

    return nb_serious_words / len(clean_title)
