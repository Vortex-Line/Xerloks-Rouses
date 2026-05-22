import os
from google import genai

gemini_api_key = os.getenv('GEMINI_API_KEY')
print(gemini_api_key)

client = genai.Client(api_key = gemini_api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)