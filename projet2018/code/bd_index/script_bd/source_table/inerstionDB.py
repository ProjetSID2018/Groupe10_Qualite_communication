
import  json 
import mysql.connector
config = {
  'user': 'DBIndex_user',
  'password': 'password_DBIndex_user',
  'host': '127.0.0.1',
  'database': 'DBIndex',
  'raise_on_warnings': True,
}
print(config["database"])

#Recuperation des donnees Json

def get_jsonparsed_data(url):
    testFile = open(url)
    result = json.load(testFile)
    return result
    
data = get_jsonparsed_data("/var/www/html/projet2018/code/bd_index/script_bd/source_table/test_sem.json")

#Connexion a la base de donnees
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
for elem in data:
	for th in data[elem]:
		data_tt = data[elem][th]
		cursor.execute("""INSERT INTO Log (id_u, datelog, user, use_case, action) VALUES(%(id)s, %(datelog)s,%(user)s, %(use_case)s, %(action)s )""", data_tt)		
	
cnx.commit()	
cursor.close()

cnx.close()