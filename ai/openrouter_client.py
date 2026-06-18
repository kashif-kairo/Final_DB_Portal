
import requests
import certifi

 
import os
API_KEY = os.getenv("OPENROUTER_API_KEY")
 
 
def ask_llm(prompt):
 
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat-v3",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        verify=False
    )
 
    data = response.json()
 
    return data["choices"][0]["message"]["content"]
 

 