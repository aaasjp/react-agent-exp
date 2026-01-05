
from langchain.tools import tool
from typing import Any, Optional, cast
from langchain_core.runnables.config import P
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

print("====== Environment Variables ======")
print(f"TAVILY_API_KEY: {os.getenv('TAVILY_API_KEY')}")
print(f"API_KEY: {os.getenv('API_KEY')}")
print(f"BASE_URL: {os.getenv('BASE_URL')}")
print(f"MODEL: {os.getenv('MODEL')}")
print("================================")

llm = ChatOpenAI(
    model=os.getenv("MODEL"), 
    api_key=os.getenv("API_KEY"), 
    base_url=os.getenv("BASE_URL"),
    extra_body={"chat_template_kwargs": {"enable_thinking": False}}
)

import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

agent = create_deep_agent(
    model=llm,
    tools=[internet_search],
    system_prompt=research_instructions
)


'''
result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

# Print the agent's response
print(result["messages"][-1].content)
'''