from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, wrap_tool_call


from langchain.messages import ToolMessage, HumanMessage

from langchain.tools import tool
from langchain_tavily import TavilySearch
from typing import Any, Optional, cast

import os
from dotenv import load_dotenv
load_dotenv()



basic_model = ChatOpenAI(
    model=os.getenv("MODEL"), 
    api_key=os.getenv("API_KEY"), 
    base_url=os.getenv("BASE_URL"),
    extra_body={"chat_template_kwargs": {"enable_thinking": False}}
)
advanced_model = ChatOpenAI(
    model=os.getenv("MODEL"), 
    api_key=os.getenv("API_KEY"), 
    base_url=os.getenv("BASE_URL"),
    extra_body={"chat_template_kwargs": {"enable_thinking": True}}
)

@wrap_model_call
async def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = advanced_model
    else:
        model = basic_model

    return await handler(request.override(model=model))


@tool
def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    wrapped = TavilySearch(max_results=3, include_raw_content=False)
    search_results = cast(dict[str, Any], wrapped.invoke({"query": query}))
    '''
    print(f"Query: {search_results['query']}")
    for result in search_results["results"]:
        print(f"Title: {result['title']}")
        print(f"Content Snippet: {result['content']}")
        print(f"URL: {result['url']}")
        print(f"Score: {result['score']}")
        print("-"*100)
    '''
    return search_results

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"


tools = [search, get_weather]



@wrap_tool_call
async def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return await handler(request)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"]
        )


agent = create_agent(
    model=basic_model,  # Default model
    tools=tools,
    middleware=[dynamic_model_selection, handle_tool_errors],
    system_prompt="You are a helpful assistant. Your answer must be accurate. before you answer,you should think carefully!"
)

'''
result = agent.invoke(
    {"messages": [HumanMessage("金融实证方法是什么？")]}
)
print("="*150)
print(result)
print("="*150)
for msg in result["messages"]:
    #print(msg.pretty_print())
    print(type(msg))
    print(msg)
    print("-"*150)
'''