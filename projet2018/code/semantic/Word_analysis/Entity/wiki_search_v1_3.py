# Group 6 LAFONT Nicolas, QUESNOT Sandy, VAYSSE Robin
# Version 1.3 : modification of the 1.2 version, add a error gestion and
# comments
# If the wikipedia page does not exists, the home page is displayed
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import wikipedia as wk


def wikipedia_search(named_entity):

    """
    in : string of characters corresponding to a named entity
    out : url link of the wikipedia page associating to a namerd entity, type =
        string of characters
    This function looking for the named entity on wikipedia and return the url
    link.
    """

    wk.set_lang("fr")
    try:
        search = wk.search(named_entity)[0].replace(' ', '_')
    except:
        return('https://fr.wikipedia.org/wiki/')
    url_begin = 'https://fr.wikipedia.org/wiki/'
    return url_begin + search
