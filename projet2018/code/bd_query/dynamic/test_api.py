##### GROUP 3 - Version 1.0 #####
from flask import Flask, request, jsonify
import json
import requests
from flask_restful import Resource, Api
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb


app = Flask(__name__) # we are using this variable to use the flask microframework
api = Api(app)

# MySQL configurations
servername = "localhost"
username = "DBIndex_user"
passwordDB = "password_DBIndex_user"
databasename = "DBIndex"

db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)

def to_json(keys, values):
	dictionary_final = dict()
	for i in range(len(values)):
		dictionary = dict()
		for j in range(len(values[i])):
			dictionary[keys[j]]=values[i][j]
		dictionary_final[str(i+1)]=dictionary

	json = jsonify(dictionary_final)
	return json

@app.route("/Top10_source/", strict_slashes = False, methods = ['GET'])
def api_Top10_source():
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
		"source": "test",
		"nombre": 783
	}}

	result = jsonify(data)
	result.status_code = 200
	result.headers.add('Access-Control-Allow-Origin','*')
	result.headers.add('allow_redirects',True)

	return result

@app.route("/MostPublishedCat/", strict_slashes = False, methods = ['GET'])
def api_MostPublishedCat():
	data = data = {
	'1': {
		"name": "France",
		"pourcentage" : "50%"
	}}
	result = jsonify(data)
	result.status_code = 200
	result.headers.add('Access-Control-Allow-Origin','*')
	result.headers.add('allow_redirects',True)

	return result
	
@app.route("/argumentJson/<int:num_id>", strict_slashes = False, methods = ['GET'])
def api_argumentJson(num_id):
	query = """select date_publication, rate_positivity, rate_negativity, rate_joy from article where id_article = """+str(num_id)+""";"""
	cursor = db.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	
	keys = ['date_publication','rate_positivity','rate_negativity','rate_joy']
	json_file = to_json(keys,result)
	
	#json_file = jsonify(data)
	json_file.status_code = 200
	json_file.headers.add('Access-Control-Allow-Origin','*')
	json_file.headers.add('allow_redirects',True)

	return json_file
	
@app.route("/Top10_pertinent/", strict_slashes = False, methods = ['GET'])
def api_Top10_pertinent():
	data = {
	'1': {
		"text": "figaro",
		"weight" : 1
	},
	'2':{
		"text": "monde",
		"weight": 2
	},
	'3':{
		"text": "depeche",
		"weight" : 3
	},
	'4':{
		"text": "set",
		"weight": 4
	},
	'5':{
		"text": "truc",
		"weight" : 5
	},
	'6':{
		"text": "ouai",
		"weight": 6
	},
	'7':{
		"text": "plus",
		"weight" : 7
	},
	'8':{
		"text": "trente",
		"weight": 8
	},
	'9':{
		"text": "aller",
		"weight" : 9
	},
	'10':{
		"text": "test",
		"weight": 10
	}}	
	result = jsonify(data)
	result.status_code = 200
	result.headers.add('Access-Control-Allow-Origin','*')
	result.headers.add('allow_redirects',True)

	return result
	
@app.route("/json", methods = ['GET'])
def api_json():
	#tupleu = ((9,'toto','kiki'),(7,'tata','kaka'),(3,'toti','koko'),(2,'tati','bleod'))
	#keys = ['nombre','article','analyse']
	#db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	query = """select date_publication, rate_positivity, rate_negativity, rate_joy from article;"""
	cursor = db.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	#data = {
	  # '1': {
		   # "source": "figaro",
		   # "nombre" : 210
	   # },
	   # '2':{
		   # "source": "monde",
		   # "nombre": 2015
	   # },
	   # '3':{
		   # "source": "depeche",
		   # "nombre" : 50
	   # }}
	cursor.close()
	#db.close()

	keys = ['date_publication','rate_positivity','rate_negativity','rate_joy']
	result_json = to_json(keys, result)
	
	result = jsonify(result)
	result.status_code = 200
	result.headers.add('Access-Control-Allow-Origin','*')
	return result
	

# @app.route("/connectDBjson/", methods = ['GET','POST'])
# def api_connectDBjson():
	# db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	# print("connexion reussie")
	
	# # with open("bla.txt", "rb") as fin:
		# # j = json.load(fin)
	
	# # query = """select * from lemma"""
	# # cursor = db.cursor()
	# # cursor.execute(query)
	# # result = cursor.fetchall()
	# # cursor.close()
	# # 
	
	
	# res = (("mot1", 23), ("mot2", 17), ("mot3",9))
	
	# result_json = jsonify(dict(res))
	# print("ok")
	
	# # headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	
	# # repo = requests.post('http://130.120.8.250:5002/test_g3/', headers=headers, data=result_json)

	# # url = "http://130.120.8.250:5002/static_day"
	# # headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	# # r = requests.post(url, data=result_json)
	# # print(jsonify(repo.json()))
	# # res = jsonify(repo.json())
	# # res.status_code = 200
	# # res.headers.add('Access-Control-Allow-Origin','*')	# print(jsonify(repo.json()))
	# # res = jsonify(repo.json())
	# # res.status_code = 200
	# # res.headers.add('Access-Control-Allow-Origin','*')
	# return result_json
 
 
@app.route("/transfertJson/", methods = ['GET','POST'])
def api_transfertJson():
	try:
		# db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		# print("connexion reussie")
		# query = """select * from lemma"""
		# cursor = db.cursor()
		# cursor.execute(query)
		# result = cursor.fetchall()
		# cursor.close()
		# db.close()
		# result_json = jsonify(result)
		# print(result)
		
		
		headers = {'Content-Type': 'application/json'}
		data = {
			   "Period": "2018-01-05 - 2018-01-11",
			   "10_tf_idf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [],
				   [0.4563]
			   ],
			   "10_tf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [],
				   [2]
			   ],
			   "12_tf_idf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [0.6413],
				   []
			   ],
			   "12_tf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [1],
				   []
			   ],
			   "13_tf_idf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [0.2413],
				   []
			   ],
			   "13_tf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [2],
				   []
			   ],
			   "15_tf_idf": [
				   [0.1243],
				   [],
				   [0.4563],
				   [0.1543],
				   [],
				   [],
				   []
			   ],
			   "15_tf": [
				   [4],
				   [],
				   [4],
				   [3],
				   [],
				   [],
				   []
			   ],
			   "17_tf_idf": [
				   [],
				   [],
				   [],
				   [],
				   [0.7883],
				   [],
				   []
			   ],
			   "17_tf": [
				   [],
				   [],
				   [],
				   [],
				   [6],
				   [],
				   []
			   ],
			   "21_tf_idf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [0.3113],
				   []
			   ],
			   "21_tf": [
				   [],
				   [],
				   [],
				   [],
				   [],
				   [8],
				   []
			   ],
			   "23_tf_idf": [
				   [],
				   [],
				   [],
				   [0.2713],
				   [],
				   [],
				   []
			   ],
			   "23_tf": [
				   [],
				   [],
				   [],
				   [5],
				   [],
				   [],
				   []
			   ],
			   "25_tf_idf": [
				   [],
				   [0.3583],
				   [],
				   [],
				   [],
				   [],
				   []
			   ],
			   "25_tf": [
				   [],
				   [3],
				   [],
				   [],
				   [],
				   [],
				   []
			   ],
			   "100_tf_idf": [
				   [0.4113],
				   [],
				   [],
				   [],
				   [],
				   [],
				   []
			   ],
			   "100_tf": [
				   [9],
				   [],
				   [],
				   [],
				   [],
				   [],
				   []
			   ]
			}
		#data = jsonify(data)
		print(type(data))
		repo = requests.post('http://130.120.8.250:5002/static_week/', headers=headers, data=data) ###############################
		
		#url = "http://130.120.8.250:5002/static_day"
		#headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
		#r = requests.post(url, data=data)
		print(repo.json())
		res = jsonify(repo.json())
		res.status_code = 200
		res.headers.add('Access-Control-Allow-Origin','*')
		return res
		
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
		


# @app.route("/selectweb/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
# def api_selectweb():
	# db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	# print("connexion reussie")
	# query = """select * from lemma"""
	# cursor = db.cursor()
	# cursor.execute(query)
	# result = cursor.fetchall()
	# cursor.close()
	# print(result)
	# db.close()
	# return "select ok"

	

# @app.route("/insertweb/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
# def api_insertweb():
	# try:
		# db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		# print("connexion reussie iw")
		# query = """insert into lemma (lemma) values ('tata');"""
		# cursor = db.cursor()
		# cursor.execute(query)
		# db.commit()
		# cursor.close()
		# db.close()
		# return "insert ok"
		
	# except mysql.connector.Error as err:
		# if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			# print("Something is wrong with your user name or password")
		# elif err.errno == errorcode.ER_BAD_DB_ERROR:
			# print("Database does not exist")
		# else:
			# print(err)


# @app.route("/hello/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
# def sayHello():
	# return "salam"

# # @app.route("/theme", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
# # def api_theme():
	# # jour=request.form['jour']
	# # print(jour)
	# # res={'nombre':10,'source':'lemonde'}
	# # jres=json.dump(res)
	# # print(jres)
	# # return jres
	

if __name__ == '__main__':
	app.run(host="130.120.8.250", port = 5000, debug = True)