# api/gemini.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def explain_to_sql(explanation, db_type="mysql",model="gemini-2.0-flash"):
    prompt = f"""
    Convert the following user explanation into an SQL query for a {db_type} database:

    Explanation: "{explanation}"

    SQL:
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        res_json = response.json()
        if 'candidates' not in res_json:
            raise ValueError(f"Gemini API Error: {res_json.get('error', 'Unknown error')}")
        return res_json['candidates'][0]['content']['parts'][0]['text'].strip()
    
    except Exception as e:
        return f"Error: {e}"
