from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain.agents.middleware import SummarizationMiddleware
load_dotenv()


agent = create_agent(
    model="gpt-4o-mini",
    system_prompt='You are a helpful assistant',
    checkpointer=InMemorySaver(),
    middleware=[SummarizationMiddleware(
        model="gpt-4o-mini",
        keep=('messages', 4),
        trigger=('messages', 6)
    )])

questions = [
    {"role": "user", "content": "Hi, My name is Tejas. Can you remember that?"},
    {"role": "user", "content": "What is 2+2?"},
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "user", "content": "What is the current weather in New York?"},
    {"role": "user", "content": "What is the largest mammal?"},
    {"role": "user", "content": "What is the meaning of life?"}
]


config = {
    'configurable': {
        'thread_id': 'my_thread_id'
    }
}

for question in questions:
    response = agent.invoke({'messages' : [question]}, config=config)
    print(f"Messages: {response['messages']}")
    print(f"Length of messages: {len(response['messages'])}")
