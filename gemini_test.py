import os
import requests

print("Starting Gemini test...")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: API key is not set.")
    exit()

print("API key found.")
print("Connecting to Gemini...")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

data = {
    "contents": [{
        "parts": [{
            "text": "Say hello to a student."
        }]
    }]
}

try:
    response = requests.post(
        url,
        params={"key": API_KEY},
        json=data,
        timeout=20
    )

    print("Status:", response.status_code)
    print(response.text)

except requests.exceptions.Timeout:
    print("ERROR: Connection timed out.")

except Exception as e:
    print("ERROR:", e)
