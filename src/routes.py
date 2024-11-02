from src import app
import requests
from os import getenv
from dotenv import load_dotenv
from .forms import SummarizeForm
from flask import render_template
load_dotenv()
AUTH = getenv('AUTH')
app.secret_key = "secret"


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
        "x-use-cache": "false"

    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()


@app.route('/')
def home():
    routse = [i.endpoint for i in app.url_map.iter_rules()]
    del routse[0:2]
    return render_template('home.html', routes=routse)


@app.route('/summarize', methods=["GET", 'POST'])
def summarize():
    form = SummarizeForm()
    if form.validate_on_submit():
        text = form.text.data
        model_id = "facebook/bart-large-cnn"
        response = get_response_from_model(
            model_id,
            {
                "inputs": text,
                "parameters": {
                    "max_length": 300, "min_length": 50, "do_sample": False,
                },
            })
        result = response[0].get("summary_text")

        form.result.data = result

    return render_template('summarize.html', form=form)
