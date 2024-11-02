from src import app
import requests
from os import getenv
from dotenv import load_dotenv
from .forms import SummarizeForm, InputForm
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


@app.route('/summarize', methods=["GET", 'POST'])
def summarize():
    form = SummarizeForm()
    if form.validate_on_submit():
        text = form.text.data
        model_id = "meta-llama/Llama-3.2-3B-Instruct"
        response = get_response_from_model(
            model_id,
            {
                "inputs": f"Summarize the following text without adding any introductory phrases or extra text: {text}",
                "parameters": {"return_full_text": False,
                               "watermark": False,
                               "do_sample": True,  # Enable sampling to get different responses
                               "top_k": 50,        # Top-k sampling
                               "top_p": 0.95       # Top-p (nucleus) sampling
                               },
            })
        result = response[0].get("generated_text").splitlines()
        # del result[0:3]
        form.result.data = "\n".join(result)

    return render_template('summarize.html', form=form)

@app.route('/translate')
def translation():
    """
    """
    from transformers import M2M100Tokenizer

    form = InputForm()

    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    print(get_response_from_model("facebook/m2m100_418M",
    {
        "inputs": form.input.data,
        "parameters": {
                        "forced_bos_token_id": tokenizer.get_lang_id("en"),
        }
    }
))
