import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(encoding='utf8')
# Access the API key using the variable name defined in the .env file
api_key = os.getenv("OPENAI_API_KEY")

# defininig the HTTP headers for API reqyest
headers = {
    "Authorization": f"Bearer {api_key}"
}

# sending a POST request using the v1 GPT /completions API with the requied headers and prompt from user
response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json={
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "max_tokens": 100
    }
)

print(response.json())
