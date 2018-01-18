###############################################################################
# -*- coding: utf-8 -*-
"""
GROUPE 6 : ANALYSE SEMANTIQUE
AUTEURS : QUENTIN MARCU, ROBIN VAYSSE, ADIL ZOUITINE
VERSION : 1.1
"""
# -*- coding: utf-8 -*-
##############################################################################

from __future__ import absolute_import, division, print_function
import pandas as pd
from difflib import SequenceMatcher
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from time import time


# FR/EN : input() output(series[Dataframe])
def loadData():
    """
    EN : Loading dataset
    FR : charge le jeu de données
    """
#    path='FEEL_clean.csv'
    path = 'Article_analysis/Polarity/FEEL_clean.csv'
    df = pd.read_csv(path, sep=';')
    return(df)


# FR/EN : input(string) output(list)
def Tokenize(text):
    """
    EN : Split text on list of word
    FR : sépare un texte en liste de mot
    """
    return word_tokenize(text)


# FR/EN : input(list) output(list)
def del_stop_word_list(list_text):
    """
    EN: Delete stop words of list
    FR :  suprimme les mot vide [stop words] d'une liste
    """
    new_list = []
    stop = stopwords.words('french')
    stop.append("les")
    stop.append(".")
    stop.append("!")
    stop.append("?")
    stop.append(",")
    stop.append(";")
    stop.append(":")
    stop.append("(")
    stop.append(")")
    stop.append("[")
    stop.append("]")
    stop.append("«")
    stop.append("»")
    stop.append('"')
    for i in list_text:
        if i not in stop:
            new_list.append(i)
    return new_list


# FR/EN : input(list) output(string)
def List_to_text(list_word):
    return ' '.join(list_word)


# FR/EN : input(string) output(list)
def Text_to_list(text):
    """
    EN : Convert text on list without stop words
    FR :  transforme un texte en liste [sans mot vide]
    """
    return del_stop_word_list(Tokenize(text))


# FR/EN : input(string,string) output(float [0,1])
def similar(word1, word2):
    """
    EN : Give a similarity rate between two strings
    FR :  donne un pourcentage de similarité entre les chaines de caractère
    """

    """
    EN : How Work SequenceMatcher function
    Sequence matcher: Compares all characters between the two words
    and counts the similarities.
    Do the same thing again, taking the second word backwards and counting
     it back similarities.

    FR : Comment marche la fonction SequenceMatcher
    Sequence matcher :Compare tous les caractères entre les deux mots
    et compte les similitudes.
    Refais pareil en prenant le deuxième mot à l'envers et recompte
    les similitudes.
    Le ratio se calcule par (2 * NbTotSim / TailleMot)
    """
    return SequenceMatcher(None, word1.lower(), word2.lower()).ratio()


# FR/EN : input(string,dataframe[Series]) output(int,[string/OPTIONAL])
def similar_word(word, df, return_word=False):
    """
    EN : returns the word nearest to our dataset
    in relation to any word.
    FR : retourne le mot le plus proche de notre jeu de données
    par rapport à un mot quelconque.
    """
    """
    EN : How optimization works:
    number of times the execution time of the code is reduced
    (40 allows the minimum number of operations[593] in the worst case)
    must be a 14120 divider (data frame size)
    FR : Comment marche l'optimisation :
    nombre de fois ou le temps d'execution du code est diminué
    (40 permet le nombre minimal d'opération[593] dans le pire des cas)
    /!\ doit être un diviseur de 14120  (taille du dataframe)
    """
    nb_div_df = 40
    len_df = len(df.word)
    nb_elmt_subset = int(len_df/nb_div_df)
    # EN : Index_cut list of limit terminals of the subset
    # FR : Index_cut=list des bornes des subset
    index_cut = list(range(nb_elmt_subset - 1, len_df-1, nb_elmt_subset))
    num_df = index_cut[0]
    for i in index_cut:
        if word > df.loc[i, 'word']:
            num_df = i
    """
    EN : creates a smaller dataset (nb_div_df times smaller)
    or the word is necessarily present (less calculation therefore).
    FR :  crée un jeu de données plus petit (nb_div_df fois plus petit)
    ou le mot est forcement présent (moins de calcul donc)
    """
    df_new = df[num_df: num_df + nb_elmt_subset]
    best_index = 0
    best_neighbor = 0
    best_similar = 0
    for i in df_new.index:
        word_bag_of_word = df_new.loc[i, 'word']
        """
        EN : retains the word that is most similar in relation to
        the words of the data set.
        FR : retient le mot etant le plus similaire par rapport
        aux mots du jeu de données.
        """
        similar_word = similar(word_bag_of_word, word)
        if similar_word > best_similar:
            best_similar = similar(word_bag_of_word, word)
            best_neighbor = word_bag_of_word
            best_index = i

            if best_similar == 1:  # EN : if the word is directly found,
                                    # EN : the index is directly returned.
                                    # FR : si le mot est directement trouvé on
                                    # FR :revoie directement l'index
                return best_index
            elif best_similar == 1 and return_word:  # EN : managing the
                                                    # EN : default setting.
                                                    # FR :gestion du paramètre
                                                    # FR :par défaut
                return(best_index, best_neighbor)
        if return_word:  # EN : managing the default setting.
                        # FR : gestion du paramètre par défaut
            return(best_index, best_neighbor)
    return(best_index)


# FR/EN : input(string,series[Dataframe]) output(dict)
def Feel_polarity_word(word, df, affichage_vect_polarity=False):
    """
     EN : calculates the polarity of a word returns a dictionary corresponding
     EN : to a facet.
     EN : {Anger: 1 joy: 0 } for example
     FR : calcul la polarité d'un mot
     FR : retourne un dictionaire correspondant à une facette
     FR : {colère : 1 joie : 0 } par exemple
    """
    best_index = similar_word(word, df)  # EN : finds the most matching word
    # EN : in the data set
    # FR:trouve le mot correspondant
    # FR : le plus dans le jeu de données
    vector_polarity = df.iloc[best_index]

    if affichage_vect_polarity:  # EN : managing the default setting.
                                # FR :  gestion du paramètre par défaut
        print(vector_polarity)
    vector_polarity = vector_polarity.to_dict()  # EN : Convert Series in dict
    # FR : convertit Series en dict
    return vector_polarity


# FR/EN : input(list,series[Dataframe]) output(list)
def Feel_polarity_text(list_word, df):
    """
    FR : Calcule la polarité  de tout les mots de la liste de mot et
    met dans une liste chaque dictionnaire de polarité
    """
    list_dict_polarity_word = []
    for word in list_word:
        # FR : met dans une liste chaque dictionnaire de polarité
        # EN : puts each polarity dictionary into a list
        list_dict_polarity_word.append(Feel_polarity_word(word, df))
    return list_dict_polarity_word


# FR/EN : input(dict) output(dict)
def Del_word(dict_pol):
    """
    EN : deletes key and word value from dictionary
    FR : supprime la clé et la valeur word du dictionnaire
    """
    return dict_pol.pop('word', None)


# FR/EN : input(list) output(list)
def list_del_word(list_dico):
    """
    EN : deletes the key and the word veleur from the dictionary
    a dictionary list
    FR : supprime la clé et la veleur word du dictionnaire
    d'une liste de dictionaire
    """
    for i in range(0, len(list_dico)):
        Del_word(list_dico[i])
    return list_dico


# FR/EN : input(dict,int) output(dict)
def ratio_dict(dico, nb_word_text):
    """
    EN :  divides all dictionary values by nb_word_text
    FR : divise toutes les valeurs d'un dictionnaire par nb_word_text
    """
    for key in dico.keys():
        # dico[key] = round((dico[key] / nb_word_text),2)
        dico[key] = dico[key] / nb_word_text
    return dico


# FR/EN : input(list) output(list)
def list_ratio_dict(list_dico):
    """
    EN :divides all dictionary values by nb_word_text
    for a whole list of dictionaries
    FR : divise toutes les valeurs d'un dictionnaire par nb_word_text
    pour tout une liste de dictionnaire
    """
    taille_list_dico = len(list_dico)
    for i in range(0, taille_list_dico):
        list_dico[i] = ratio_dict(list_dico[i], taille_list_dico)
    return list_dico


# FR/EN : input(dict,dict) output(dict)
def Sum_dico(Dict1, Dict2):
    """
    EN : sum up two dictionaries
    FR : fais la somme de deux dictionnaires
    """
    return dict(Counter(Dict1) + Counter(Dict2))


# FR/EN : input(list) output(dict)
def Sum_list_dico(list_dico):
    """
    EN : add the sum of n dictionary by adding them two by two
    FR : fais la somme de n dictionnaire en les additionnant deux à deux
    """
    taille_dico = len(list_dico)
    if taille_dico == 1:
        return(list_dico[0])
    sum_list_dico = Sum_dico(list_dico[0], list_dico[1])
    if taille_dico == 2:
        return(sum_list_dico)
    if taille_dico > 2:
        for i in range(2, taille_dico):
            sum_list_dico = Sum_dico(sum_list_dico, list_dico[i])
    return(sum_list_dico)


# FR/EN : input(list) output(dict)
def Feel_polarity_aggregate(list_word):
    """
    EN : calculates the average of the polarity of a word list
    FR : calcule la moyenne des polarité d'une liste de mot
    """
    df = loadData()
    list_vecteur_polarite = Feel_polarity_text(list_word, df)
    list_dico_clean = list_del_word(list_vecteur_polarite)
    list_dico_ration = list_ratio_dict(list_dico_clean)
    res_dico = Sum_list_dico(list_dico_ration)
    return(res_dico)


# FR/EN : input(string) output(dict)
def Feel_polarity_main(text):
    """
    EN : Calculates the average polarity of a text
    FR : Calcule la polarité moyenne d'un texte
    """
    list_word = Text_to_list(text)  # EN : converts the text into a word list
    # EN : because the function that calculates the polarity
    # EN :takes only the word lists.
    # FR : convertit le text en liste de mot
    # FR : car la fonction qui calcule la polarité prend que les listes de mot
    resultat = Feel_polarity_aggregate(list_word)
    return(resultat)

if __name__ == '__main__':

    print(Feel_polarity_main("je vous déteste"))
    start = time()
    text_tweet_macron = ("Comme pour beaucoup de Français,la Chine est pour "
                         "moi un pays fascinant, la plus ancienne civilisation"
                         "vivante,un « État plus vieux que l'Histoire » disait"
                         "le Général de Gaulle.")
    print("\n",
          Feel_polarity_main(text_tweet_macron),
          "\n",
          "Temps d'execution : ",
          time() - start)
