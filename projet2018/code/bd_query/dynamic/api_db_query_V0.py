##### GROUP 3 - Version 1.0 - RY/RV/MC/CR/EM : Creation des requetes #####
##### GROUP 3 - Version 1.1 - MC/CR : modification des requetes #####
##### GROUP 3 - Version 1.2 - MC/CR : Rajout des commentaires #####

from flask import Flask, request, jsonify
import json
import requests
from flask_restful import Resource, Api
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__) # we are using this variable to use the flask microframework
#api = Api(app)

# MySQL configurations
servername = "localhost"
username = "DBIndex_user"
passwordDB = "password_DBIndex_user"
databasename = "DBIndex"

def to_json(keys, values):
	"""
	input : keys = list of keys for the json file
			values = values related to the keys
	output : json file
	
	This function create a json file in a predefined format (for G9)
	"""
	dictionary_final = dict()
	for i in range(len(values)):
		dictionary = dict()
		for j in range(len(values[i])):
			dictionary[keys[j]]=values[i][j]
		dictionary_final[str(i+1)]=dictionary

	json = jsonify(dictionary_final)
	return json

def execute_query(query) :
	"""
	input : the query
	output : dict object (we have to turn it into a json object with the "to_json" function)
	
	Task Automation (creating a cursor, execute the query, return the result)
	"""
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result	
	
##query 1 Web
@app.route("/frequency_word_week/", methods = ['GET', 'POST'])	
def api_frequency_word_week():
	"""
	input : 
	output : return a json file
	
	View the most common keywords of the week
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	query = """SELECT w.word, count(w.word)
			   FROM article a, word w,lemma l, position_word pw 
			   WHERE w.id_lemma = l.id_lemma
			   AND w.id_word = pw.id_word
			   AND pw.id_article = a.id_article
			   AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
			   GROUP BY w.word 
			   ORDER BY 2 DESC LIMIT 10;"""
	result = execute_query(query)
	keys = ['text','weight']
	json_file = to_json(keys,result)
	
	db.close()
	json_file.status_code = 200
	json_file.headers.add('Access-Control-Allow-Origin','*')
	json_file.headers.add('allow_redirects',True)
	return json_file
		
##query 2 Web 
@app.route("/percent_Theme/<string:vTheme>", methods = ['GET', 'POST'])
def api_percent_Theme(vTheme):
	"""
	input :
	output : json file
	
	Show theme and percentage of number of articles
	of this theme for the week
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	query = """ SELECT la.label, ((count(a.id_article)/(SELECT count(id_article) FROM article))*100) 
				INTO vTheme, vPercent
				FROM article a, belong b, label la 
				WHERE la.label = """+vTheme+"""
				AND b.id_label = la.id_label 
				AND b.id_article = a.id_article
				AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE; 
				"""
	result = execute_query(query)
	keys = ['name','pourcentage']
	json_file = to_json(keys,result)
	db.close()
	json_file.status_code = 200
	json_file.headers.add('Access-Control-Allow-Origin','*')
	json_file.headers.add('allow_redirects',True)
	return json_file
		
##query 3 Web : 
@app.route("/Top_10_source/", methods = ['GET', 'POST'])	
def api_Top_10_source():
	"""
	input :
	output : json file
	
	Top 10 sources with the most articles per week 
	(name of the source and number of articles)
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	query = """SELECT n.name_newspaper, count(a.id_article)
			   FROM article a , newspaper n
			   WHERE n.id_newspaper = a.id_newspaper
			   AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
			   GROUP BY n.name_newspaper
			   ORDER BY 2 DESC LIMIT 10;"""
	result = execute_query(query)
	keys = ['source','nombre']
	json_file = to_json(keys,result)
	db.close()

	json_file.status_code = 200
	json_file.headers.add('Access-Control-Allow-Origin','*')
	json_file.headers.add('allow_redirects',True)
	return json_file

		
##query 4 Web ### Fonction à vérifier
@app.route("/link_by_source/", methods = ['GET', 'POST'])	
def api_link_by_source():
	"""
	input :
	output : json file
	
	For each source, retrieve the link + the link of the image
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	query = """SELECT DISTINCT n.name_newspaper, n.link_newspaper, n.link_logo
			   FROM newspaper n;"""
	result = execute_query(query)
	keys = ['source','lien_source','lien_logo']
	json_file = to_json(keys,result)
	db.close()
	
	return json_file
		
##query 5 Web : Most answered words / week for the selected theme
@app.route("/frequency_Theme/<String:vTheme>", methods = ['GET', 'POST'])	
def api_frequency_Theme(vTheme):
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """CREATE PROCEDURE frequency_Theme (INOUT vTheme VARCHAR(50)) 
				BEGIN
					SELECT la.label, w.word, count(w.word)
					FROM article a, label la, word w, lemma l, position_word pw,
					belong b 
					WHERE w.id_lemma = l.id_lemma
					AND w.id_word = pw.id_word
					AND pw.id_article = a.id_article
					AND a.id_article = b.id_article
					AND la.id_label = b.id_label
					AND la.label = vTheme
					AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
					ORDER BY 3 DESC LIMIT 5;
				END;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		
		
##query 7 Web : Frequency of appearance of the word per week
@app.route("/count_word_Theme/<String:vTheme>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_count_word_Theme(vTheme):
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """CREATE PROCEDURE count_word_Theme (INOUT vTheme VARCHAR(50)) 
				BEGIN
					SELECT la.label, w.word, count(w.word)
					FROM article a, label la, word w, lemma l, position_word pw,
					belong b 
					WHERE w.id_lemma = l.id_lemma
					AND w.id_word = pw.id_word
					AND pw.id_article = a.id_article
					AND a.id_article = b.id_article
					AND la.id_label = b.id_label
					AND la.label = vTheme
					AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
					ORDER BY 3 DESC LIMIT 5;
				END;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
	
##query 8 Web : Frequency of the word by source
@app.route("/frequency_per_Word/<String:vSource>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_frequency_per_Word(vSource):
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """CREATE PROCEDURE frequency_word_per_source  (INOUT vSource varchar(50), OUT vPercent FLOAT, OUT vWord varchar(50))
				BEGIN
				   SELECT w.word, count(pw.id_word) INTO vWord, vPercent
				   FROM word w, lemma l, position_word pw, article a, newspaper n
				   WHERE w.id_lemma = l.id_lemma
				   AND w.id_word = pw.id_word
				   AND pw.id_article = a.id_article
				   AND n.id_newspaper = a.id_newspaper
				   AND n.name_newspaper=vSource;
				END;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"

		

##query 9 Web : List of words associated with the keyword
@app.route("/list_Key_Word/<String:vWord>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_list_Key_Word(vWord):
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """CREATE PROCEDURE list_Key_Word (INOUT vWord varchar(50), OUT vSynonym varchar(50)) 
				BEGIN
					SELECT s.synonym INTO vSynonym
					FROM   word w, lemma l, synonym s
					WHERE w.id_lemma = l.id_lemma
					AND w.id_synonyme = s.id_synonyme
					AND w.word = vWord;
				END;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		
##query 10 Web : Frequency of appearance of the word by theme		
@app.route("/frequency_Word_Theme/<String:vWord>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_frequency_Word_Theme(vWord):
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """CREATE PROCEDURE frequency_Word_Theme (INOUT vWord varchar(50), OUT vfrequency FLOAT, OUT vlabel varchar(25))
				BEGIN
					SELECT la.label, w.word, count(pw.id_word) INTO vlabel, vWord, vfrequency
					FROM article a, belong b, label la, word w, lemma l, position_word pw   
					WHERE w.id_lemma = l.id_lemma
					AND w.id_word = pw.id_word
					AND pw.id_article = a.id_article
					AND la.id_label = b.id_label
					AND b.id_article = a.id_article
					AND w.word = vWord
					GROUP BY la.label, w.word;
				END;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		

##query 11 Web : count the number of newspapers
@app.route("/number_newspaper/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_number_newspaper():
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """SELECT count(n.id_newspaper)
			   FROM newspaper n;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		

##query 12 Web: bring out all the newspaper names
@app.route("/title_newspaper/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_title_newspaper():
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """SELECT DISTINCT n.name_newspaper
			   FROM newspaper n;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		
##query 13 Web : number of items
@app.route("/number_items/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_number_items():
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """SELECT number_article 
			   FROM mv_number_article_week ;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		
##query 14 Web : number of items/labels	
@app.route("/number_items_per_label/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_number_items_per_label():
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie iw")
	query = """SELECT id_label,number_article
			   FROM mv_number_article_week_label ;"""
	cursor = db.cursor()
	cursor.execute(query)
	db.commit()
	cursor.close()
	db.close()
	return "insert ok"
		
		
	
if __name__ == '__main__':
	app.run(host="130.120.8.250", port = 5007, debug = True)
	
