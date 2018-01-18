from flask import Flask, request
import json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

semantic = {}


class Test_Semantic(Resource):
    def get(self, sem_id):
        return {sem_id: semantic[sem_id]}

    def put(self, sem_id):
        semantic[sem_id] = request.get_json()
        return {sem_id: semantic[sem_id]}


api.add_resource(Test_Semantic, '/<string:sem_id>')

if __name__ == '__main__':
    app.run(port = '5005')