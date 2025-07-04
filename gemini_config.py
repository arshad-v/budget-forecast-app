import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GeminiAPI:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
    
    def generate_response(self, input_text):
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": input_text
                        }
                    ]
                }
            ]
        }
        response = requests.post(self.endpoint, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"API Error: {response.status_code} - {response.text}"