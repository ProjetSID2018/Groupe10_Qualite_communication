import sys
import json
from itertools import chain
from collections import defaultdict

from flask import jsonify
from flask import Flask, request
from flask_restful import Resource, Api


sys.path.append('/var/www/html/projet2018/code/stat/static')
from function import test_trend, file_trend, score_day, score_week

app = Flask(__name__)
api = Api(app)

### Ne pas supprimer cette fonction / Do not delete this function
@app.route("/test_g3/", methods = ['GET', 'POST'])
def api_test_g3():
	day = request.get_json()
	print(day)
	res = {'nombre':10,'source':'lemonde', 'data': day }
	return jsonify(res)

@app.route("/static_day/", methods = ['GET', 'POST'])
def api_static_day():
	day = request.get_json()
	score = score_day(day, 10)[1]
	score_word_cloud = score_day(day, 10)[0]
	result_trend = file_trend(score)
	result = defaultdict(list)
	for k, v in chain(score_word_cloud.items(), result_trend.items()):
   		 result[k].append(v)		
	return jsonify(result)


@app.route("/static_week/", methods = ['GET', 'POST'])
def api_static_week():
	week = request.get_json()
	print(type(week))
	print(week)
	top_word_week = score_week(week, 10)[0]
	return jsonify(top_word_week)



@app.route("/static_month", methods = ['GET', 'POST'])
def api_static_months():
	month = request.get_json()
	print(month)
	res={'nombre':10,'source':'lemonde'}
	jres=json.dump(res)
	print(jres)
	return jres	


@app.route("/static_day_by_type", methods = ['GET', 'POST'])
def api_static_day_word():
	day = request.get_json()
	print(day)
	res={'nombre':10,'source':'lemonde'}
	jres=json.dump(res)
	print(jres)
	return jres

@app.route("/static_week_by_type", methods = ['GET', 'POST'])
def api_static_week_word():
	week = request.get_json()
	print(week)
	res={'nombre':10,'source':'lemonde'}
	jres=json.dump(res)
	print(jres)
	return jres

@app.route("/static_month_by_type", methods = ['GET', 'POST'])
def api_static_month_word():
	month = request.get_json()
	print(month)
	res={'nombre':10,'source':'lemonde'}
	jres=json.dump(res)
	print(jres)
	return jres

if __name__ == '__main__':
    app.run(host = "130.120.8.250", port = 5002, debug = True)