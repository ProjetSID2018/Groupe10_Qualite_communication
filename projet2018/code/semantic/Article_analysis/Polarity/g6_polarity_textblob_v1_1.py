###############################################################################
# -*- coding: utf-8 -*-
"""
GROUPE 6 : ANALYSE SEMANTIQUE
AUTEURS : QUENTIN MARCU, ADIL ZOUITINE
VERSION : 1.0
"""
# -*- coding: utf-8 -*-
###############################################################################

from textblob import TextBlob # sentiment en fr
from textblob_fr import PatternTagger, PatternAnalyzer

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

def blob_resultat(polarity, subjectivity):
    # reduce value field [-1,1] to [0,1]
    positivity = (0.5*polarity)+0.5
    negativity = 1-((0.5*polarity)+0.5)
    if positivity >= negativity:
        winner= 'positive'
    else:
        winner = 'negativity'
    res={'polarity_positive': positivity,
         'polarity_negative': negativity,
         'label': winner,
          'subjectivity': subjectivity}
    return(res)

def blob_main(text):

    polarity, subjectivity = blob_sentiment(text)
    return(blob_resultat(polarity, subjectivity))
    
        
if __name__ == '__main__': 
    print('\n')
    text_tweet_macron = ("Comme pour beaucoup de Français,la Chine est pour "
                         "moi un pays fascinant, la plus ancienne civilisation"
                         "vivante,un « État plus vieux que l'Histoire » disait"
                         "le Général de Gaulle.")
    print(blob_main(text_tweet_macron))