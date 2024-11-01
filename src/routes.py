from src import app
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()
AUTH = getenv('AUTH')


def get_response_from_model(model_id, data: dict) -> dict:
    """_summary_

    Args:
        model_id (string): like "facebook/bart-large-cnn"
        data (dict): input data to the model and praameters

    Returns:
        dict: response from the model
    """
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"

    headers = {
        "Authorization": f"Bearer {AUTH}",
        "Content-Type": "application/json",
        "x-wait-for-model": "true",

    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()
