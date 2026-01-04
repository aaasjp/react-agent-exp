from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver  
import os
from langchain_openai import ChatOpenAI
from langchain.tools import tool

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL"), 
    api_key=os.getenv("API_KEY"), 
    base_url=os.getenv("BASE_URL"),
    extra_body={"chat_template_kwargs": {"enable_thinking": False}}
)


@tool
def get_user_info(name: str) -> str:
    """
    Get the user info.
    args:
        name: the name of the user
    returns:
        the age of the user
    """
    return f"User {name} is 25 years old."

agent = create_agent(
    llm,
    tools=[get_user_info],
    checkpointer=InMemorySaver(),  
)


''''
print("-------------Turn 1-------------------")
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Hi! My name is Bob."}]},
    {"configurable": {"thread_id": "1"}},  
)

for msg in result["messages"]:
    print(msg.pretty_print())

print("-------------Turn 2-------------------")
result = agent.invoke(
    {"messages": [{"role": "user", "content": "do you know my age?"}]},
    {"configurable": {"thread_id": "1"}},  
)

for msg in result["messages"]:
    print(msg.pretty_print())

print("-------------Turn 3-------------------")
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is my name?"}]},
    {"configurable": {"thread_id": "1"}},  
)

for msg in result["messages"]:
    print(msg.pretty_print())


print("-------------Turn 4-------------------")
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is my name?"}]},
    {"configurable": {"thread_id": "2"}},   ## new thread
)

for msg in result["messages"]:
    print(msg.pretty_print())

'''