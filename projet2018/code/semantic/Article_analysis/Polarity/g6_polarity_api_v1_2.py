###############################################################################
# -*- coding: utf-8 -*-
"""
GROUPE 6 : ANALYSE SEMANTIQUE
AUTEURS : QUENTIN MARCU, ADIL ZOUITINE
VERSION : 1.0
"""
# -*- coding: utf-8 -*-
##############################################################################
import requests  # api
import json


def api_polarity(text, lang='french',
                 link='http://text-processing.com/api/sentiment/'):

    data = [
        ('language', str(lang)),
        ('text', str(text)), ]

    response = requests.post(link, data=data)
    if response == 400:
        error_res = ("Mauvaise requête : texte vide ou dépasse "
                     "les 80000 caractères")
        return(response, error_res)
    elif response == 503:
        error_res = "Vous avez depassé les 1000 rêquetes par jour sur cette IP"
        return(response, error_res)
    else:
        return(response, response.content)


def api_polarity_clean(response):
    response_string = response.decode("utf-8", "ignore")
    response_clean = response_string[15:]
    response_clean = response_clean[:-17]
    return response_clean


def api_polarity_string(contenue):
    json_acceptable_sting = contenue.replace("'", "\"")
    dict_api = json.loads(json_acceptable_sting)
    return dict_api


def api_polarity_dict(dict_api):
    del dict_api["neutral"]
    dict_api['polarity_negative'] = dict_api.pop('neg')
    dict_api['polarity_positive'] = dict_api.pop('pos')
    if dict_api['polarity_negative'] > dict_api['polarity_positive']:
        dict_api['label'] = "negative"
    else:
        dict_api['label'] = "positive"
    return dict_api


def api_polarity_main(_, value):
    value = api_polarity_clean(value)
    value = api_polarity_string(value)
    value = api_polarity_dict(value)
    return value


if __name__ == '__main__':
    _, value = api_polarity('Notre groupe est fou mais travailleur')
    value = api_polarity_clean(value)
    value = api_polarity_string(value)
    value = api_polarity_dict(value)
    print(value)
