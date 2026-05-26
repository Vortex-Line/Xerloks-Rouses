from openrouter import OpenRouter
import os

api_key = "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"

def ia_chat():
    while True:
        user_input = input("Você: ")

        with OpenRouter(
            api_key=api_key
        ) as client:
            response = client.chat.send(
                model="openai/gpt-oss-120b:free",
                messages=[
                    {'role': 'system', 'content': 'Você é uma IA especialista em descobrir se uma informação que está na internet é verdadeira ou falsa, responda de forma curta.'},
                    {"role": "user", "content": user_input}
                ]
            )
            
            print("Ia: ", response.choices[0].message.content)

ia_chat()
