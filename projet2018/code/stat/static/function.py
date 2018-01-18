import numpy
import scipy.stats


def score_day(file,top_word):
    
    """
    the function's objectives :
        This function allows you to show the most important words of a newspaper 
        article and the TF of the previous day and the day for each word.
        
        We place the number of words what we want in parameters of the function 
        when we call it.
        
    the function's parameters : 
        The two function's parameters are 
        - the file json which contains datas
        - the number of words what we want
        
    the function returns 
        - a dictionnary which contains the key words and their mean on two days
        - a dictionnary wich contains the key words and all corresponding values 
    
    """
    agregate=0
    counter=0
    key_word={}
    dico_tf={}
    #calculate mean TF IDF by word 
    for key,val in file.items():
        if key!="period" :
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate=agregate+val[index1][index2]
                    counter=counter+1
                   
            mean_word=round(agregate/counter,2)

            key_word[key]=mean_word

            agregate=0
            counter=0
            
    #sort words in descending order
    key_word_sort=sorted(key_word.items(),reverse=True, key=lambda t: t[1])
    
    #get only the number of key word pick by user
    key_word=key_word_sort[0:top_word]
    
    #get TF IDF of key word 
    dico_back={}
    for k, v in key_word:
        dico_back[k] = v

    #construct the value dictionary for each word        
    list_agregate=[]
    dico={}
    for key_dico_back in dico_back.keys():
        dico_tf[key_dico_back]=file.get(key_dico_back)
    for key,val in dico_tf.items():
        for index1 in range(len(val)):
            if len(val[index1])!= 0 :
                for index2 in range(len(val[index1])):
                    list_agregate.append(val[index1][index2])
            else :
                list_agregate.append(0)
        dico[key]=list_agregate
        list_agregate=[]
    dico["period"]=file.get("period")

    
    return(dico_back,dico)


def test_trend(data, word, id_day):
    ''' This function has three parameters :
    data : json data
    word : words to analyse 
    id_day :  day to analyse 
    This function calculate the T-test for the means of two independent samples and returns the conclusion of the test
	'''
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Tendance_en_hausse')
        elif (test[0] < 0):
            return(word, 'Tendance_en_baisse')
        else:
            return(word, 'Pas_de_Tendance')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Tendance_fortement_en_hausse')
        elif (test[0] < 0):
            return(word, 'Tendance_fortement_en_baisse')
        else:
            return(word, 'Pas_de_Tendance')
    else:
        return(word, 'Pas_de_tendance')


def file_trend(data):
    """ data preprocessing for groupe 9
    param : data -> json data
    return json with trend, period and most important word"""
    dict = {}
    for cle, valeur in data.items():
        if(cle != 'period'):
            for val in range(1, len(valeur)):
                word, trend = test_trend(data, cle, val)
            dict[cle] = trend
        else:
            dict[cle] = valeur
    return(dict)

def score_week(file, top_word):
    '''
Function calculate mean TF IDF by word to built a dictionnary of word most
important
Function has two parameters:
    file : Json File
    top_word : number of important word which user would
It returns a dictionnary of top word with their mean TF IDF
A second dictionnary with top word with their TF values
'''''
    agregate = 0
    counter = 0
    key_word = {}
    dictionnary_intermediate = {}
    list_mean_intermediate = []

    # calculate mean TF IDF by word
    for key, val in file.items():
        if key[-3:] == "idf":
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate = agregate + val[index1][index2]
                    counter = counter + 1
                if counter == 0:
                    list_mean_intermediate.append(0)
                else:
                    list_mean_intermediate.append(agregate/counter)

            key_word[key[:-7]] = numpy.mean(list_mean_intermediate)
            agregate = 0
            counter = 0

    # trier les mots par ordre décroissant
    key_word_sort = sorted(key_word.items(), reverse=True, key=lambda t: t[1])

    # get only the number of key word pick by user
    key_word = key_word_sort[0:top_word]

    # get TF IDF of key word
    dico_back = {}
    for k, v in key_word:
        dico_back[k] = v

    # built a intermediate dictionnary of TF by word
    liste_agregate = []
    dico_tf = {}
    for key_dico_back in dico_back.keys():
        wrd = key_dico_back + "_tf"
        dictionnary_intermediate[wrd] = file.get(wrd)
    # built dictionnary of TF
    for key, val in dictionnary_intermediate.items():
        k = key[:-3]  # remove terminaison
        for index1 in range(len(val)):
            if len(val[index1]) != 0:
                for index2 in range(len(val[index1])):
                    agregate = agregate + val[index1][index2]
            else:
                agregate = 0
            liste_agregate.append(agregate)
            agregate = 0
        dico_tf[k] = liste_agregate
        liste_agregate = []
    return(dico_back, dico_tf)



