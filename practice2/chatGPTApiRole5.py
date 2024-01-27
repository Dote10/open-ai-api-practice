import openai
import os
from dotenv import load_dotenv

load_dotenv()

 
openai.api_key =  os.getenv("OPEN_AI_API_KEY")

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user", "content": "2002년 월드컵에서 가장 화제가 되었던 나라는 어디야?"}, 
            ]
        )

print(response.choices[0].message.content)
