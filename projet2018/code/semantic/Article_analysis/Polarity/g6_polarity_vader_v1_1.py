###############################################################################
# -*- coding: utf-8 -*-
"""
GROUPE 6 : ANALYSE SEMANTIQUE
AUTEURS : QUENTIN MARCU, ADIL ZOUITINE
VERSION : 1.0
"""
# -*- coding: utf-8 -*-
##############################################################################
from __future__ import absolute_import, division, print_function
import pydeepl # traduction
from nltk.sentiment.vader import SentimentIntensityAnalyzer # sentiment en anglais



def traduction_x_to_y(text,affichage = False,from_language = 'FR',to_language = 'EN'): # traduit de français à l'anglais à l'aide de Deepl
                                                                                        # le meilleur traducteur en ligne actuel 

    translation = pydeepl.translate(text, to_language, from_lang=from_language)
    if affichage == True :
        print(translation)
    return translation

def polarity_vader(text_en,affichage = False): # n'acepte que les texte en anglais, calcule la polarité
    sid = SentimentIntensityAnalyzer()
    polarity = sid.polarity_scores(text_en)
    if affichage == True :
        print(polarity)
    return polarity

if __name__ == '__main__': 
    translate=traduction_x_to_y("C'est triste,tu as vu il pleut",affichage= True)
    print('\n')
    polarity_vader(translate,affichage= True)
    print('\n')
