from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model  = ChatOpenAI(model ="gpt-4o-mini")

response = model.stream("Draft a 1000 words essay on the importance of learning programming languages in today's world.")

for chunk in response:
    print(chunk.text, end = "", flush = True)