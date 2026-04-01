from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location"""
    return f"The current weather in {location} is sunny with a temperature of 25°C."


agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_current_weather]
)

messages = [
    {"role": "user", "content": "What is the current weather in New York?"}
]
response = agent.invoke({
    'messages': messages
})

print(response['messages'][-1].content)