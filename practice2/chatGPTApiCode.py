import openai
import os
from dotenv import load_dotenv

load_dotenv()

 
openai.api_key =  os.getenv("OPEN_AI_API_KEY")

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": "Tell me briefly how to make a pizza"}]
        )

print(response)
print(response.usage)


  
