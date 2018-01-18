from __future__ import absolute_import, division, print_function
import os 
from nltk.corpus import wordnet as wn # pour les synonymes 
import requests # api
import re
from textblob import TextBlob # sentiment en fr
from textblob_fr import PatternTagger, PatternAnalyzer
from nltk.tag import StanfordPOSTagger # pos tag
import pydeepl # traduction
from nltk.sentiment.vader import SentimentIntensityAnalyzer # sentiment en anglais
from nltk import ne_chunk, pos_tag, word_tokenize # reconaissance des entitées nommées
from nltk.tree import Tree


def synonyme(word):
    return [synset.lemma_names('fra') for synset in wn.synsets(word,lang='fra')][1]

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

   



 #Chunk permet d'avoir les entitées nommée.
def get_continuous_chunks(text): # code pris sur stack overflow (améliorable)
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     prev = None
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk
     # si on veux savoi si il s'agit d'un lieu ect ect 
     #for i in ne_chunk(pos_tag(word_tokenize(my_sent))): il faut travailler sur ça
         #print(i)


if __name__ == '__main__': 
    # code de test
    word='Chien'
    test=synonyme(word)
    print(test)
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

    my_sent = "Donald Trump est un homme d'affaire. Steve Jobs est un membre de l'entreprise Apple mais aussi il est le créateur de iPhone. Bill Gate est le créateur de Microsoft. Monsieur Macron est le président de la France."
    entity=get_continuous_chunks(my_sent)
    print(entity)
    # OUT : ['Donald Trump', 'Steve Jobs']