from openrouter import OpenRouter
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
api_key = os.getenv('OPEN_ROUTER_API_KEY')

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