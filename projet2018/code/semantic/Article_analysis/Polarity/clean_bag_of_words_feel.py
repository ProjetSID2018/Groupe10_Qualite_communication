from __future__ import absolute_import, division, print_function
import os
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
 

def loadData():
        df=pd.DataFrame.from_csv('/home/side/Documents/M1 SID/Projet SID/FEEL.csv',sep=';')
        return(df)
df=loadData()
df=pd.get_dummies(df,columns = ['polarity'] )
stop = stopwords.words('french')
df['word']= df['word'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
df=df.dropna(axis=0,how="all")
df = df[df['word']!='']
#df=df.drop([2353])
#df=df.reset_index()
df.to_csv('FEEL_clean.csv', sep=';', index=True)