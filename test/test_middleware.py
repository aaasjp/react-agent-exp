from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
        model=os.getenv("MODEL"),  # Specify a model available on OpenRouter
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
        extra_body={"chat_template_kwargs": {"enable_thinking": False}}
    )

@tool
def weather_tool(city: str) -> str:
    """Get the weather in a city"""
    return f"The weather in {city} is sunny."

@tool
def calculator_tool(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

agent = create_agent(
    model=model,
    tools=[weather_tool, calculator_tool],
    middleware=[
        SummarizationMiddleware(
            model=model,
            trigger=("tokens", 4000),
            keep=("messages", 20),
        ),
    ],
)
'''
result = agent.invoke({"messages": [{"role": "user", "content": "What is the weather in Tokyo?"}]})
for msg in result["messages"]:
    print(msg.pretty_print())
'''