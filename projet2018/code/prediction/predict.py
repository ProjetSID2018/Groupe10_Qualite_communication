# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import requests
import pickle

from recoding import Recoding


def predict():
# Import our classifier and articles to predict
   vectorizer = pickle.load(open('vectorizer', 'rb'))
   model = pickle.load(open('clf', 'rb'))
   recode = Recoding()
   data = recode.recode_data(recode.import_data())
   df = data[data['theme'] != 'delete']
   art_to_predict = data[data['theme'] == 'delete']
   xtrain = vectorizer.transform(art_to_predict['list_lemma']).toarray()
   predicted = model.predict(xtrain)
   #predicted = predicted.argmax(1) #Proba to selected label
   
   dict_inv_classes = {
               0:'international',
               1:'france',
               2:'economie',
               3:'sciences_high_tech',
               4:'arts_et_culture',
               5:'sports',
               6:'sante'
               }
   
   cat_pred = pd.Series(predicted).map(dict_inv_classes)
   art_to_predict['theme'] = list(cat_pred)
   df = pd.concat([df, art_to_predict])
   
   res = [
          { "id_article":i, "label": j} for (i,j) in zip(df['id'], df['theme'])    
          ]
   
   return res
   
res = predict()

#res = [{"id_article":56, "label":"sante"}, {"id_article":2, "label":"sciences_high_tech"}, {"id_article":18, "label":"sante"}]
url ='http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/API/index/belong'
r = requests.post(url=url, json=res[0:2])
print(r.text)
r = requests.post(url=url, json=[res[2]])
print(r.text)
#r = requests.post(url=url, json=res[:100])
#r = requests.post(url=url, json=res[100:200])
#print(r.text)