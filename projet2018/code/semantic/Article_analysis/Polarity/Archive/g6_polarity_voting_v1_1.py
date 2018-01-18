###############################################################################
# -*- coding: utf-8 -*-
"""
GROUPE 6 : ANALYSE SEMANTIQUE
AUTEURS : QUENTIN MARCU, ADIL ZOUITINE
VERSION : 1.0
"""
# -*- coding: utf-8 -*-
##############################################################################

import json


from .g6_polarity_feel_1_0 import *
from .g6_polarity_textblob_1_0 import *
from .g6_polarity_vader_1_1 import *


def openjson(filename):

    with open(filename, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return json_data


def all_method(text):
    resultat = {'feel': None, 'textblob': None } #, 'vader': None}
    resultat['feel'] = Feel_polarity_main(text)
    resultat['textblob'] = blob_main(text)
    # resultat['vader'] = polarity_vader_main(text)
    return resultat

def aggregation_all_method(resultat):
    dict_poids = {'feel' : 0.7, 'textblob' : 0.3 } # , 'vader' : 0.3}
    res = {}
    resultat['feel']['polarity_negative'] *= dict_poids['feel']
    resultat['feel']['polarity_positive'] *= dict_poids['feel']
    resultat['textblob']['polarity_negative'] *= dict_poids['textblob']
    resultat['textblob']['polarity_positive'] *= dict_poids['textblob']
    # resultat['vader']['polarity_negative'] *= dict_poids['vader']
    # resultat['vader']['polarity_positive'] *= dict_poids['vader']
    res['polarity_negative'] = resultat['feel']['polarity_negative'] + resultat['textblob']['polarity_negative']# + resultat['vader']['polarity_negative']
    res['polarity_positive'] = resultat['feel']['polarity_positive'] + resultat['textblob']['polarity_positive']# + resultat['vader']['polarity_positive']
    if res['polarity_negative'] > res['polarity_positive']:
        res['label'] = 'negative'
    else:
        res['label'] = 'positive'
    res['fear'] = resultat['feel']['fear']
    res['anger'] = resultat['feel']['anger']
    res['disgust'] = resultat['feel']['disgust']
    res['sadness'] = resultat['feel']['sadness']
    res['surprise'] = resultat['feel']['surprise']
    res['subjectivity'] = resultat['textblob']['subjectivity']
    return res

    """
    on parcours tout les dico et on récupère la valeur pol_pos et pol_neg
    multiplié par leur poids associé et on additionne le tout dans résultat   
    """
    """ on y ajoute après toutes les autres polarité """
    
    
def gestion_key(dict_json):
    list_key = []
    for key in dict_json.keys():
        list_key.append(key)
    if 'polarity_positive' in list_key:
        dict_json['rate_positivity'] = dict_json.pop('polarity_positive')
    else:
        dict_json.update({'rate_positivity' : 0})
    if 'polarity_negative' in list_key:
        dict_json['rate_negativity'] = dict_json.pop('polarity_negative')
    else:
        dict_json.update({'rate_negativity' : 0})
    if 'joy' in list_key:
        dict_json['rate_joy'] = dict_json.pop('joy')
    else:
        dict_json.update({'rate_joy' : 0})
    if 'fear' in list_key:
        dict_json['rate_fear'] = dict_json.pop('fear')
    else:
        dict_json.update({'rate_fear' : 0})
    if 'sadness' in list_key:
        dict_json['rate_sadness'] = dict_json.pop('sadness')
    else:
        dict_json.update({'rate_sadness' : 0})
    if 'anger' in list_key:
        dict_json['rate_angry'] = dict_json.pop('anger')
    else:
        dict_json.update({'rate_angry' : 0})
    if 'surprise' in list_key:
        dict_json['rate_surprise'] = dict_json.pop('surprise')
    else:
        dict_json.update({'rate_surprise' : 0})
    if 'disgust' in list_key:
        dict_json['rate_disgust'] = dict_json.pop('disgust')
    else:
        dict_json.update({'rate_disgust' : 0})
    if 'subjectivity' in list_key:
        dict_json['rate_subjectivity'] = dict_json.pop('subjectivity')
    else:
        dict_json.update({'rate_subjectivity' : 0})
    return dict_json
    
    
def aggregation_main(text):
    resultat = all_method(text)
    resu = aggregation_all_method(resultat)
    return resu


def aggregation_main_json(filename):
    text = openjson(filename)
    List_word_article = text['content']['words']
    for i in range(0,len(List_word_article)):
        List_word_article[i] = List_word_article[i].lower()
    List_word_article = del_stop_word_list(List_word_article)
    text_article = List_to_text(List_word_article)
    aggreg_text_article = aggregation_main(text_article)
    aggreg_text_article = gestion_key(aggreg_text_article)
    del aggreg_text_article['label']  #For V2
    del aggreg_text_article['rate_subjectivity']  #For V2
    for key in aggreg_text_article.keys():
        aggreg_text_article[key] ='{:.3f}'.format(aggreg_text_article[key])
    return aggreg_text_article


def dict_to_json(dict_res,filename):
    with open(filename, 'w', encoding = "utf-8") as fp:
        json.dump(dict_res, fp)
        

def out_polarity_json(filename, aggreg_text_article):
    In=openjson(filename)
    out= {}
    out.update({'name_author': In['author']})
    out.update({'date_publication' :In['date_publi']})
    out.update({'name_newspaper' :In['newspaper']})
    for key, value in aggreg_text_article.items():
        out.update({key : value})
    return out


def in_polarity_out(filename):
    out = aggregation_main_json(filename)
    out = out_polarity_json(filename, out)
    return out

    