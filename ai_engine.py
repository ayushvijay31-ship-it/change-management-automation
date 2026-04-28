import os
import requests

API_KEY = os.getenv("CLAUDE_API_KEY")  # set later

def analyze_change_request(description):
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 200,
        "messages": [
            {
                "role": "user",
                "content": f"Analyze this change request and respond with APPROVE or REJECT with reason:\n{description}"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["content"][0]["text"]
    else:
        return f"Error: {response.text}"
