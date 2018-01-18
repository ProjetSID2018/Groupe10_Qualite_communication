# Group 6 LAFONT Nicolas, QUESNOT Sandy, VAYSSE Robin
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

in : an article and it id.
out : a list of dictionary for each words of the article.

This function create a list of words with wikipedia link or a synonym.

"""
import sys
sys.path.insert(0, 'Word_analysis/Synset')
import g6_wordnet_synonym_V1_6 as syno

sys.path.insert(0, 'Word_analysis/Entity')
import wiki_search_v1_3 as wiki
import json


def create_wiki_syno(file, id_article):
    fic = open(file)
    text = json.load(fic)
    content = text['content']
    liste_result = []
    for key in content.keys():
        if key != 'words' and key != 'list_lemma':
            result = {}
            result['position'] = key
            result['title'] = content[key]['title']
            result['word'] = content[key]['word']
            result['type_entity'] = content[key]['type_entity']
            result['pos_tag'] = content[key]['pos_tag']
            result['id_article'] = id_article

            if result['type_entity'] != 'Null':
                result['file_wiki'] = wiki.wikipedia_search(result['word'])
                result['synonym'] = ''
            elif result['pos_tag'] in ['STOPWORD', 'DET']:
                result['file_wiki'] = 'NULL'
                result['synonym'] = ''
            else:
                result['file_wiki'] = 'NULL'
                result['synonym'] = syno.give_the_first_wordnet_synonym(result['word'])

            liste_result.append(result)
    #liste_result = json.dumps(liste_result, ensure_ascii=False)
    return liste_result
