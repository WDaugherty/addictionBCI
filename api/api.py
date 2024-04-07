from random import randint
import requests
from flask import Blueprint
from flask_restful import Resource, Api
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID")
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


def error(message):
    return message, 400


class ApiPing(Resource):
    def get(self):
        return dict(status='success', message='pong!'), 200

class Call(Resource):
    def get(self):
        # random answer
        answer = dict(random_number=(randint(0, 100)))
        return answer, 200

class R2R(Resource):
    def get(self, query):
        # Define the SciPhi API URL for the /search endpoint
        api_url = "https://sciphi-00a22a29-a66f-4564-912d-cf783fc8c3bd-qwpin2swwa-ue.a.run.app/search"
        
        data = {'query': 'Help me prevent the need to smoke again?'}

        response = requests.post(api_url, json=data)
        return response

class Neurosity(Resource):
        def get (self):
            # Define the Neurosity API URL for the /search endpoint
            api_url = "https://api.neurosity.co"
            
            # Set your API key here
            api_key

            return 

api.add_resource(Neurosity, '/api/neurosity')
api.add_resource(R2R, '/api/r2r')
api.add_resource(ApiPing, '/api/ping')
api.add_resource(Call, '/api/call')
