from langdetect import detect

from transformers import M2M100Tokenizer
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


def translate(text: str, language: str, max_tokens: int = 150) -> str:
    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    tokenized_text = tokenizer.encode(text)

    chunks = [tokenized_text[i:i + max_tokens]
              for i in range(0, len(tokenized_text), max_tokens)]
    translated_chunks = []

    for chunk in chunks:
        chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
        result = get_response_from_model("facebook/m2m100_418M",
                                         {
                                             "inputs": chunk_text,
                                             "parameters": {
                                                 "forced_bos_token_id": tokenizer.get_lang_id(language),
                                             }
                                         }
                                         )
        translated_chunks.append(result[0].get("generated_text"))

    return " ".join(translated_chunks)


def detect_language(text: str) -> str:
    return detect(text)[:2]


def summarize(text: str, model_id: str = "facebook/bart-large-cnn") -> str:
    lang = detect_language(text)
    if lang != "en":
        text = translate(text, "en")
    response = get_response_from_model(
        model_id,
        {
            "inputs": text,
            "parameters": {
                "do_sample": False,
            },
        })
    result = response[0].get("summary_text")
    if lang != "en":
        result = translate(result, lang)
    return result
