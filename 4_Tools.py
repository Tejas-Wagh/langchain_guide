from langchain_openai import ChatOpenAI
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location"""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

model = ChatOpenAI(model = "gpt-4o-mini")

model_with_tools = model.bind_tools([get_current_weather])
messages = [{
    'role':'user',
    'content':'What is the current weather in New York?'
}]

response = model_with_tools.invoke(messages)
print(response)
