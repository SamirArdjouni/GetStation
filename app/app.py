import flask
import pymongo
import json
from flask_cors import CORS, cross_origin


class App:
    def __init__(self, params: dict) -> None:
        self.__mongo = pymongo.MongoClient(params["mongo_host"], params["mongo_port"])
        self.__db = self.__mongo[params["mongo_db"]]
        
        self.__app = flask.Flask(__name__)
        CORS(self.__app)
        
        self.__app.add_url_rule("/route", "action", self.action, methods=['POST'])
        
    @cross_origin()
    def action(self):
        try:
            return flask.Response(json.dumps({}), status=200, mimetype="application/json")
        except Exception as e:
            return_message = {
                "message": str(e)
            }
            return flask.Response(json.dumps(return_message), status=400, mimetype="application/json")
    
    def run(self):
        self.__app.run('0.0.0.0', 8000)
        