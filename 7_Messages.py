from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi"),
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)