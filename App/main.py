from openrouter import OpenRouter
import os

api_key = "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"

user_input = input("Você: ")

with OpenRouter(
    api_key=api_key
) as client:
    response = client.chat.send(
        model="openai/gpt-oss-120b:free",
        messages=[
            {"role": "user", "content": user_input + " responde de forma curta"}
        ]
    )
    
    print("Ia: ", response.choices[0].message.content)
