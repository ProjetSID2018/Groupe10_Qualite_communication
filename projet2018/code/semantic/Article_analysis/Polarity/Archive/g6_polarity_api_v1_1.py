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


if __name__ == '__main__':
    _, contenue = api_polarity('mauvaise vie')
    print(contenue)
    print('\n')
    _, contenue2 = api_polarity("Je vous crève j'espère que"
                                "tu vas mourir violé")
    print(contenue2)
    print('\n')
