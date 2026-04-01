from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain.tools import tool

@tool
def express_evaluator(expression: str) -> str:
    """Evaluate a mathematical expression and return the result."""
    try:
        result = eval(expression)
        return f"The result of the expression '{expression}' is: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

search_tool = TavilySearch(
    max_results=3,
    topic='general'
)


agent = create_agent(
    model="gpt-4o-mini",
    system_prompt='You are a helpful assistant',
    tools=[express_evaluator,search_tool]
)


for step in agent.stream({
    'messages': 'Who won cricket world cup in 2026 and what is 2+2?'},
    stream_mode='values'
):
    print(step['messages'][-1].pretty_print())



# print(response)