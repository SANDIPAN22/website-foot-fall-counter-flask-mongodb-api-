from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
client=MongoClient("localhost",27017)
db=client["database_visitors"]
col=db["visitors"]


class HelloWorld(Resource):
    def get(self):
        x=col.find()[0]["V"]
        x=x+1
        col.update({},{"$set":{"V": x}})
        return {'hello VISITOR': x }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
