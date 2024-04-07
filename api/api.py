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
        api_url = "https://sciphi-00a22a29-a66f-4564-912d-cf783fc8c3bd-qwpin2swwa-ue.a.run.app"
        
        # Set your API key here
        api_key = "your_api_key_here"
        
        # Prepare the headers and parameters for the API request
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        params = {
            "query": query,
            # Add other parameters as required by your application
        }
        
        # Make the request to the SciPhi API
        response = requests.get(api_url, headers=headers, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the API response as JSON
            return response.json()
        else:
            # Handle errors (you might want to improve this with more specific error messages)
            return {"error": "Failed to retrieve data from SciPhi API"}

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
