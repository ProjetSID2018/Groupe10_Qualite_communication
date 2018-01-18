from __future__ import absolute_import, division, print_function
import pandas as pd
from difflib import SequenceMatcher
from collections import Counter
def loadData():
    df=pd.DataFrame.from_csv('/home/side/Documents/M1 SID/Projet SID/FEEL_clean.csv',sep=';')
    return(df)


def similar(word1,word2): # donne un pourcentage de similarité entre le chaine de caractère
	return SequenceMatcher(None, word1, word2).ratio()
#Compare tous les caractères entre les deux mots et compte les similitudes.
#Refais pareil en prenant le deuxième mot à l'envers et recompte les similitudes.
#Le ratio se calcule par (2 * NbTotSim / TailleMot) 

def similar_word(word,df,return_word=False): #input(string,dataframe) output(int,[string/OPTIONAL]) retourne le mot le plus proche de notre jeu de données par rapport à un mot quelconque;
	
     best_index = 0
     best_neighbor = 0
     best_similar = 0
     for i in range(1, len(df)-1):
         word_bag_of_word=df.iloc[i]['word']
          
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

def Del_word_list_dict(list_dict):
    list_dict_clean=[]    
    for i in list_dict:
        list_dict_clean.append(Del_word(list_dict[i]))
    return list_dict_clean
    
def Sum_dict(list_dict): 
    somme= Counter({}) 
    for i in range(1,len(list_dict)-1):
        if i == 1:
            somme= Counter(list_dict[0]) + Counter(list_dict[i])
        somme= somme + Counter(list_dict[i])
    return dict(somme)
        
            

if __name__ == '__main__': 
	#test
    df=loadData()
    mot='abscent'
    print(similar_word(mot,df))
    Vecteur=Feel_polarity_word(mot,df)
    print(Vecteur)
    list_mot=["pute","salope"]
    list_vecteur_polarite=Feel_polarity_text(list_mot,df)
    list_vecteur_polarite_clean=Del_word_list_dict(list_vecteur_polarite)  
    Sum_dict(list_vecteur_polarite)
    