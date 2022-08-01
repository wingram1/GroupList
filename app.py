from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment on this deployment
import server

app = Flask(__name__, static_url_path='', static_folder='../client')
CORS(app) #comment on this deployment
api = Api(app)

@app.route('/', defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

# api.add_resource(server, '/flask/hello')