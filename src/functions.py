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
        "x-use-cache": "false"

    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()


def translate(text: str, language: str) -> str:
    """translate text to the given language

    Args:
        text (str): text to translate
        language (str): language to translate to like "ar"for Arabic

    Returns:
        str: translated text
    """
    from transformers import M2M100Tokenizer

    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    result = get_response_from_model("facebook/m2m100_418M",
                                     {
                                         "inputs": text,
                                         "parameters": {
                                             "forced_bos_token_id": tokenizer.get_lang_id(language),
                                         }
                                     }
                                     )

    print(result)

    return result[0].get("generated_text")
