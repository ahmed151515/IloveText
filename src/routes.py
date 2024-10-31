from src import app
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()
AUTH = getenv('AUTH')


def get_response(model_id, params: dict):
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"

    headers = {
        "Authorization": f"Bearer {AUTH}",
        "Content-Type": "application/json",
        "x-wait-for-model": "true",

    }
    data = {
        "inputs": "Can you please let us know more details about your ",
        "parameters": params
    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()
