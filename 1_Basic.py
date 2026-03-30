from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI


model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
response = model.invoke("What is the capital of France?")

print(response.content)
