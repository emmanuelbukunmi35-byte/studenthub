import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain Newton's first law in simple words for a secondary school student."
                }
            ]
        }
    ]
}

response = requests.post(
    url,
    params={"key": API_KEY},
    json=data
)

print("Status:", response.status_code)
print(response.text)
