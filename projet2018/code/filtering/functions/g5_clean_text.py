"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Group 5 - Filtrage
@author: Paul Lafaurie

Function : Remove all non-word non-digit character
============================================================================"""

import re

"""============================================================================
    Clean Text of all weird symbols
============================================================================"""
# Tokenization without punctuation
# @param:text actual content of the article


def clean_symbols(text):

    # Replace sentence ending punctuation by full-stop
    art = text.replace('?', '.')
    art = art.replace('!', '.')
    art = art.replace('...', '.')

    # Replace apostrophes by blanks
    art = re.sub(r'’', ' ', art)

    # Get previous letter
    prev_apostrophe = re.findall('([A-Za-z])\'', art)

    for letter in prev_apostrophe:
        art = re.sub(letter + '\'', letter + ' ', art)
        continue

    # Remove symbols and characters other than letters and digits(accents stay)
    art = re.sub(r'[^\w\s\._]', '', art, re.UNICODE)

    # Remove blanks at the beginning or the end.
    art = re.sub('^ +', '', art)
    art = re.sub(' +$', '', art)

    # Replace several consecutive blanks by just one blank.
    art = re.sub(' +', ' ', art)

    # Out: text content without unnecessary characters
    return art
