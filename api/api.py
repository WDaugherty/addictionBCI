from random import randint
import requests
from flask import Flask, request, Blueprint
from flask_restful import Resource, Api
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

load_dotenv()


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

def r2r(data):
        # URL of the external API endpoint you want to call
        api_url = "https://sciphi-00a22a29-a66f-4564-912d-cf783fc8c3bd-qwpin2swwa-ue.a.run.app/search"

        # Get data from the incoming POST request
        data = request.get_json(force=True)  # Corrected this line

        # Forward the request to the external API
        response = requests.post(api_url, json=data)

        print("Response from external API: ", response.json())
        # Return the response from the external API to the client
        return response.json(), response.status_code

class Neurosity(Resource):
        def post (self):

            print("Starting neurosity")
            neurosity = NeurositySDK({
                "device_id": os.getenv("NEUROSITY_DEVICE_ID")
            })

            neurosity.login({
                "email": os.getenv("NEUROSITY_EMAIL"),
                "password": os.getenv("NEUROSITY_PASSWORD")
            })



            def callback(data):
                print("data", data)
                # Launch drone
                r2r()

                # { probability: 0.92, label: "leftArm", timestamp: 1569961321191, type: "kinesis"  }

            print("Neurosity unsubscribe")
            unsubscribe = neurosity.kinesis("leftHandPinch", callback)

            return unsubscribe

api.add_resource(Neurosity, '/api/neurosity')
api.add_resource(ApiPing, '/api/ping')
api.add_resource(Call, '/api/call')
