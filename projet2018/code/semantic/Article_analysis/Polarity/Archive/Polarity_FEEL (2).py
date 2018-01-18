from __future__ import absolute_import, division, print_function
import pandas as pd
from difflib import SequenceMatcher
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords


def loadData():

    df=pd.DataFrame.from_csv('/home/side/Documents/M1 SID/Projet SID/FEEL_clean.csv',sep=';')
    return(df)

def Tokenize(text):
    return word_tokenize(text)

def del_stop_word_list(list_text):
    new_list = []
    stop = stopwords.words('french')
    stop.append("les")
    for i in list_text:
        if i not in stop:
            new_list.append(i)
    return new_list

def Text_to_list(text):
    return del_stop_word_list(Tokenize(text))
    
def similar(word1,word2): # donne un pourcentage de similarité entre le chaine de caractère
	return SequenceMatcher(None, word1, word2).ratio()
#Compare tous les caractères entre les deux mots et compte les similitudes.
#Refais pareil en prenant le deuxième mot à l'envers et recompte les similitudes.
#Le ratio se calcule par (2 * NbTotSim / TailleMot) 

#def similar_word(word,df,return_word=False): #input(string,dataframe[Series]) output(int,[string/OPTIONAL]) retourne le mot le plus proche de notre jeu de données par rapport à un mot quelconque;
#	
#     best_index = 0
#     best_neighbor = 0
#     best_similar = 0
#     for i in range(1, len(df)-1):
#         word_bag_of_word=df.iloc[i]['word']
#          
#         if similar(word_bag_of_word,word) > best_similar:
#             best_similar=similar(word_bag_of_word,word)
#             best_neighbor = word_bag_of_word
#             best_index= i
#              
#             if best_similar == 1 :
#                 return best_index
#             elif best_similar == 1 and return_word:
#                 return(best_index,best_neighbor)
#         if return_word:
#             return(best_index,best_neighbor)
#     return(best_index)

def similar_word(word,df,return_word=False): #input(string,dataframe[Series]) output(int,[string/OPTIONAL]) 
    #retourne le mot le plus proche de notre jeu de données par rapport à un mot quelconque;
    nb_div_df = 40 # nombre de fois ou le temps d'execution du code est diminué /!\ doit être un diviseur de 14120  (taille du dataframe)
    len_df = len(df.word)
    nb_elmt_subset = int(len_df/nb_div_df)
    index_cut = list(range(nb_elmt_subset - 1, len_df-1, nb_elmt_subset))    
    
    num_df = index_cut[0]
    for i in index_cut:
        if word > df.loc[i,'word']:
            num_df = i
    
    df_new = df[num_df : num_df + nb_elmt_subset]
    
    best_index = 0
    best_neighbor = 0
    best_similar = 0
    for i in df_new.index:
        word_bag_of_word = df_new.loc[i,'word']
       
        if similar(word_bag_of_word,word) > best_similar:
            best_similar=similar(word_bag_of_word,word)
            best_neighbor = word_bag_of_word
            best_index= i
          
            if best_similar == 1 :
                return best_index
            elif best_similar == 1 and return_word:
                return(best_index,best_neighbor)
        if return_word:
            return(best_index,best_neighbor)
    return(best_index)


def Feel_polarity_word(word,df,affichage_vect_polarity=False):
    best_index=similar_word(word,df)
    vector_polarity=df.iloc[best_index]
    
    if affichage_vect_polarity:
        print(vector_polarity)
    vector_polarity=vector_polarity.to_dict()
    return vector_polarity


def Feel_polarity_text(list_word,df):
    list_dict_polarity_word=[]
    for word in list_word:
        list_dict_polarity_word.append(Feel_polarity_word(word,df))
    return list_dict_polarity_word

def Del_word(dict_pol):
    return dict_pol.pop('word',None)

def list_del_word(list_dico):
    for i in range(0, len(list_dico)):
        Del_word(list_dico[i])
    return list_dico
    
def ratio_dict(dico, nb_word_text):
    for key in dico.keys():
        dico[key] = round((dico[key] / nb_word_text),2)
    return dico
    
def list_ratio_dict(list_dico):
    for i in range(0, len(list_dico)):
        list_dico[i] = ratio_dict(list_dico[i],len(list_dico))
    return list_dico

def Sum_dico(Dict1,Dict2):
    return dict(Counter(Dict1)+Counter(Dict2))

def Sum_list_dico(list_dico):
    taille_dico= len(list_dico)   
    if taille_dico == 1:
        return(list_dico[0])  
    sum_list_dico=Sum_dico(list_dico[0],list_dico[1])   
    if taille_dico==2 : 
        return(sum_list_dico)
    if taille_dico> 2 :
        for i in range(2,taille_dico):        
            sum_list_dico = Sum_dico(sum_list_dico,list_dico[i])
    return(sum_list_dico)

    
def agregation(list_dico_avec_nom):
    list_dico_clean=list_del_word(list_dico_avec_nom)
    list_dico_ration=list_ratio_dict(list_dico_clean)
    somme_dico=Sum_list_dico(list_dico_ration)
    return(somme_dico)

def Feel_polarity_aggregate(list_word):
    df=loadData()
    list_vecteur_polarite=Feel_polarity_text(list_word,df)
    list_dico_clean=list_del_word(list_vecteur_polarite)
    list_dico_ration=list_ratio_dict(list_dico_clean)
    res_dico=Sum_list_dico(list_dico_ration)
    return(res_dico)

def Feel_polarity_main(text):
    list_word=Text_to_list(text)
    resultat = Feel_polarity_aggregate(list_word)    
    return resultat 

if __name__ == '__main__': 
    
    print(Feel_polarity_main("Salut les fils de pute ceci est un test"))