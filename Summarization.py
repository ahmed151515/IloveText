import requests

Model_ID = "facebook/bart-large-cnn"
api_token = ""
inp = input("enter your text : ")

API_URL = f"https://api-inference.huggingface.co/models/{Model_ID}"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

data = {
    "inputs": inp  # No need for f-string here since inp is already a string
}

response = requests.post(API_URL, headers=headers, json=data)

# Check if the response is successful
if response.status_code == 200:
    result = response.json()
    print(result[0]["summary_text"])
else:
    print(f"Error: {response.status_code}, {response.text}")
