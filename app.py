from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from lib.testHandler import HelloApiHandler
from data.dbconection import db_session

app = Flask(__name__, static_url_path='', static_folder='frontend')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'default.html')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(HelloApiHandler, '/flask/hello')