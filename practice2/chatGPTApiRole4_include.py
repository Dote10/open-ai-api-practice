import openai
import os
from dotenv import load_dotenv

load_dotenv()

 
openai.api_key =  os.getenv("OPEN_AI_API_KEY")

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content": "2002년 월드컵에서 가장 화제가 되었던 나라는 어디야?"}, #이전 질문
            {"role":"assistant", "content": "바로 예상을 뚫고 4강 진출 신화를 일으킨 한국입니다."},  #이전 답변
            {"role":"user", "content": "그 나라가 화제가 되었던 이유를 자세하게 설명해줘"} #마지막 질문
            ]
        )

print(response.choices[0].message.content)
