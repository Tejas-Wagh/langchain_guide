from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(model = "gpt-4o-mini")

responses = model.batch([
    'Who is the owner of Porsche?',
    'What is the capital of France?',   
    'Who is the CEO of Deloitte USI?'
])

for response in responses:
    print(response.content)