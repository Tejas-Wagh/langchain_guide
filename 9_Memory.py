from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()


agent = create_agent(
    model="gpt-4o-mini",
    system_prompt='You are a helpful assistant',
    checkpointer=InMemorySaver()
)

messages = [
    {"role": "user", "content": "Hi, My name is Tejas. Can you remember that?"},
]

config = {
    'configurable': {
        'thread_id': 'my_thread_id'
    }
}
response = agent.invoke({'messages' : messages}, config=config)

print(response['messages'][-1].content)


response = agent.invoke({'messages' : [
    {"role": "user", "content": "What is my name?"}
]}, config=config)

print(response['messages'][-1].content)