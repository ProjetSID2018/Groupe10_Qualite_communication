from __future__ import absolute_import, division, print_function
import os 
import requests # api
import re
from textblob import TextBlob # sentiment en fr
from textblob_fr import PatternTagger, PatternAnalyzer
import pydeepl # traduction
from nltk.sentiment.vader import SentimentIntensityAnalyzer # sentiment en anglais


# https://curl.trillworks.com  convertir le curl en request 
def api_polarity(text,lang='french',link='http://text-processing.com/api/sentiment/'):

    data = [
        ('language', str(lang)),
        ('text', str(text)),
]
    response = requests.post(link, data=data)
    if response == 400: 
        return(response,"Mauvaise requête : texte vide ou dépasse les 80000 caractères")
    elif response == 503 :
        return(response,"Vous avez depassé les 1000 rêquetes par jour sur cette IP")
    else :
        return(response,response.content) # manque à convertir le .contents en valeurs que l'on veut

def blob_sentiment(text,Polarity=True,Subjectivity=True): 
    # Utilise un fichier xml ou il y a 5300 mot ayant une polarité et une subjectivité
    # Le score de polarité est un float entre [-1,1] quand c'est égale à -1 l'opinion est négative et 1 l'opinion est positive
    # Le score de subjectivité est un float entre [0,1] quand c'est égale à 0 le texte est objectif et quand c'est égale 1 le texte est subjectif

    blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
   
    if Polarity ==True and Subjectivity ==True:
        return blob.sentiment[0],blob.sentiment[1]
    elif Polarity ==True and Subjectivity ==False:
        return blob.sentiment[0]
    elif Polarity ==False and Subjectivity ==True:
        return blob.sentiment[1]
    else:
        return None

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
    # code de test
    
    #print([synset.lemma_names('fra') for synset in wn.synsets('chien', lang='fra')])
    _,contenue=api_polarity('mauvaise vie')
    print(contenue)
    print('\n')
    pol,sub=blob_sentiment('mauvaise vie')
    print("la polarité est : ",pol," La subjectivité est : ",sub)
    print('\n')


    translate=traduction_x_to_y("C'est triste,tu as vu il pleut",affichage= True)
    print('\n')
    polarity_vader(translate,affichage= True)
    print('\n')
