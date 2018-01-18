# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:22:10 2018
@author: mathi
"""

from flask import Flask, request,  jsonify, Response
import json
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)


# @app.route('/general', methods = ['POST'])
# def general():
#     #--> requete sur la base
#     #--> appel de l'API du groupe statiques
#     
#     data = {
#         'nbart'  : 2000,
#         'source' : ["lemonde", "le figaro", "le nouvel obs"]
#     }
#     resp = jsonify(data)
#     resp.status_code = 200
#     resp.headers.add('Access-Control-Allow-Origin', '*')
#     return resp
# 
# @app.route('/theme', methods = ['GET'])
# def theme():
#     #--> requete sur la base
#     #--> appel de l'API du groupe statiques
#     word =request.args.get('word')  
#     source = request.args.get('source')  
#     print(word, source)
#     data = {
#         'src'  : source,
#         'word' :word,
#         'tendancy' : {'month':'-','week':'+','day':'+-'},
#         'verbe':{'verbe' : 'atomiser','month':'+','week':'-','day':'--'},
#         'theme':{'culture' : 1,'politic':80,'humor':19}
#     }
#     resp = jsonify(data)
#     resp.status_code = 200
#     resp.headers.add('Access-Control-Allow-Origin', '*')
#     return resp
 
##################################################
#                   PAGE INDEX                  #   
##################################################
@app.route('/test', methods = ['GET'])
def general():
    data = {
   '1': {
        "source": "figaro",
        "nombre" : 210
    },
    '2':{
        "source": "monde",
        "nombre": 2015
    },
    '3':{
        "source": "depeche",
        "nombre" : 50
    },
    '4':{
        "source": "set",
        "nombre": 45
    },
    '5':{
        "source": "truc",
        "nombre" : 544
    },
    '6':{
        "source": "ouai",
        "nombre": 45
    },
    '7':{
        "source": "plus",
        "nombre" : 76
    },
    '8':{
        "source": "trente",
        "nombre": 71
    },
    '9':{
        "source": "aller",
        "nombre" : 828
    },
    '10':{
        "source": "dix",
        "nombre": 783
    },
    '11':{
        "source": "onze",
        "nombre": 7823
    },
    '12':{
        "source": "douze",
        "nombre": 78223
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp  
   
@app.route('/test1', methods = ['GET'])
def general1():
    data = {
   '1': {
        "text": "figaro",
        "weight" : 1,
        "trend" : "hausse"
    },
    '2':{
        "text": "monde",
        "weight": 2,
        "trend" : "baisse"
    },
    '3':{
        "text": "depeche",
        "weight" : 3,
        "trend" : "normale"
    },
    '4':{
        "text": "set",
        "weight": 4,
        "trend" : "normale"
    },
    '5':{
        "text": "truc",
        "weight" : 5,
        "trend" : "normale"
    },
    '6':{
        "text": "ouai",
        "weight": 6,
        "trend" : "normale"
    },
    '7':{
        "text": "plus",
        "weight" : 7,
        "trend" : "normale"
    },
    '8':{
        "text": "trente",
        "weight": 8,
        "trend" : "normale"
    },
    '9':{
        "text": "aller",
        "weight" : 9,
        "trend" : "normale"
    },
    '10':{
        "text": "test",
        "weight": 10,
        "trend" : "normale"
    }
}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/test2', methods = ['GET'])
def general2():
    data = {
   '1': {
        "name": "France",
        "pourcentage" : "50%"
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 

@app.route('/gauge', methods = ['GET'])
def gauge():
    data = {
    '1': {
        "feeling": "Degout",
        "pourcent" : "50"
    },
    '2': {
        "feeling": "Peur",
        "pourcent" : "20"
    },
    '3': {
        "feeling": "Joie",
        "pourcent" : "80"
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 


##################################################
#                   PAGE THEME                  #   
##################################################

 
@app.route('/theme', methods = ['GET'])
def theme():
    data = {
    '1':{
        "theme" : "Art et Culture",
        "effectif" : 31090763
    },
    '2':{
        "theme" : "Economie",
        "effectif" : 61801570
    },
    '3':{
        "theme" : "Science",
        "effectif" : 73137148
    },
    '4':{
        "theme" : "Sports",
        "effectif" : 74856000
    },
    '5':{
        "theme" : "France",
        "effectif" : 79716203
    },
    '6':{
        "theme" : "International",
        "effectif" : 81902307
    },
    '7':{
        "theme" : "Santé",
        "effectif" : 141850000
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 
 
@app.route('/trend/<string:vparam1>', methods = ['GET'])
def trend(vparam1):
    #theme =request.args.get('theme')
    print(vparam1)
    data = {
    '1':{
        "mot" : "verbe",
        "tendance" : "tendance1"
    },
    '2':{
        "mot" : "Nom",
        "tendance" : "tendance2"
    },
    '3':{
        "mot" : "Adjectif",
        "tendance" : "tendance3"
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 

@app.route('/cloud/<string:vparam1>', methods = ['GET'])
def cloud(vparam1):
    print(vparam1)
    data_first = {
    '1':{
        "text" : "Lorem",
        "weight" : 13
    },
    '2':{
        "text" : "Ipsum",
        "weight" : 10.5
    },
    '3':{
        "text" : "Dolor",
        "weight" : 9.4
    },
    '4':{
        "text" : "Sit",
        "weight" : 8
    },
    '5':{
        "text" : "Amet",
        "weight" : 6.2
    },
    '6':{
        "text" : "Consectetur",
        "weight" : 5
    },
    '7':{
        "text" : "Adipiscing",
        "weight" : 5
    }}
    data_bis = {
    '1':{
        "text" : "Arbre",
        "weight" : 13
    },
    '2':{
        "text" : "Bol",
        "weight" : 10.5
    },
    '3':{
        "text" : "Cerceau",
        "weight" : 9.4
    },
    '4':{
        "text" : "Domino",
        "weight" : 8
    },
    '5':{
        "text" : "Elephant",
        "weight" : 6.2
    },
    '6':{
        "text" : "Fabriquer",
        "weight" : 5
    },
    '7':{
        "text" : "Gateau",
        "weight" : 5
    }}
    data_ter = {
    '1':{
        "text" : "Hibou",
        "weight" : 13
    },
    '2':{
        "text" : "Important",
        "weight" : 10.5
    },
    '3':{
        "text" : "Joyeux",
        "weight" : 9.4
    },
    '4':{
        "text" : "Lalala",
        "weight" : 8
    },
    '5':{
        "text" : "Mouton",
        "weight" : 6.2
    },
    '6':{
        "text" : "Négation",
        "weight" : 5
    },
    '7':{
        "text" : "Obligation",
        "weight" : 5
    }}
    if vparam1 == '_international':
        data = data_first
    elif vparam1 == '_france':
        data = data_bis
    else:
        data = data_ter
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 

##################################################
#                   PAGE RECHERCHE              #   
##################################################

@app.route('/recherche1/<string:vparam1>/<string:vparam2>/<string:vparam3>/<string:vparam4>/<string:vparam5>/<string:vparam6>', methods = ['GET'])
def recherche1(vparam1,vparam2,vparam3,vparam4,vparam5,vparam6):
    print(vparam1,vparam2,vparam3,vparam4,vparam5,vparam6)
    data = {
    '1':{
        "periode" : "w1",
        "source" : "La Dépêche",
        "nombre" : 10
    },
    '2':{
        "periode" : "w1",
        "source" : "Le Figaro",
        "nombre" : 1
    },
    '3':{
        "periode" : "w1",
        "source" : "Le Point",
        "nombre" : 12
    },
    '4':{
        "periode" : "w1",
        "source" : "Le Monde",
        "nombre" : 2
    },
    '5':{
        "periode" : "w1",
        "source" : "Libération",
        "nombre" : 9
    },
    '6':{
        "periode" : "w1",
        "source" : "Nouvelle Obs",
        "nombre" : 13
    },
    '7':{
        "periode" : "w1",
        "source" : "Telerama",
        "nombre" : 6
    },
    '8':{
        "periode" : "w1",
        "source" : "Futurasciences",
        "nombre" : 5
    },
    '9':{
        "periode" : "w1",
        "source" : "L’Humanité",
        "nombre" : 9
    },
    '10':{
        "periode" : "w2",
        "source" : "La Dépêche",
        "nombre" : 20
    },
    '11':{
        "periode" : "w2",
        "source" : "Le Figaro",
        "nombre" : 35
    },
    '12':{
        "periode" : "w2",
        "source" : "Le Point",
        "nombre" : 15
    },
    '13':{
        "periode" : "w2",
        "source" : "Le Monde",
        "nombre" : 17
    },
    '14':{
        "periode" : "w2",
        "source" : "Libération",
        "nombre" : 3
    },
    '15':{
        "periode" : "w2",
        "source" : "Nouvelle Obs",
        "nombre" : 22
    },
    '16':{
        "periode" : "w2",
        "source" : "Telerama",
        "nombre" : 8
    },
    '17':{
        "periode" : "w2",
        "source" : "Futurasciences",
        "nombre" : 3
    },
    '18':{
        "periode" : "w2",
        "source" : "L’Humanité",
        "nombre" : 6
    },
    '19':{
        "periode" : "w3",
        "source" : "La Dépêche",
        "nombre" : 15
    },
    '20':{
        "periode" : "w3",
        "source" : "Le Figaro",
        "nombre" : 5
    },
    '21':{
        "periode" : "w3",
        "source" : "Le Point",
        "nombre" : 11
    },
    '22':{
        "periode" : "w3",
        "source" : "Le Monde",
        "nombre" : 17
    },
    '23':{
        "periode" : "w3",
        "source" : "Libération",
        "nombre" : 7
    },
    '24':{
        "periode" : "w3",
        "source" : "Nouvelle Obs",
        "nombre" : 23
    },
    '25':{
        "periode" : "w3",
        "source" : "Telerama",
        "nombre" : 28
    },
    '26':{
        "periode" : "w3",
        "source" : "Futurasciences",
        "nombre" : 13
    },
    '27':{
        "periode" : "w3",
        "source" : "L’Humanité",
        "nombre" : 9
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 


if __name__ == '__main__':
    app.run(debug=True)