from langchain.agents import create_agent
from langchain.tools import tool
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL"), 
    api_key=os.getenv("API_KEY"), 
    base_url=os.getenv("BASE_URL"),
    extra_body={"chat_template_kwargs": {"enable_thinking": False}}
)

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""

    return f"It's always sunny in {city}!"

agent = create_agent(
    llm,
    tools=[get_weather],
)

print("-------------stream mode: updates-------------------")
for chunk in agent.stream(  
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    stream_mode="updates", ## or values
):
    for step, data in chunk.items():
        print("--------------------------------")
        print(f"step: {step}")
        #print(f"content: {data['messages'][-1].content_blocks}")
        print(f"data: {data}")
        print(f"message numbers: {len(data['messages'])}") ## validate the stream mode is updates

print("-------------stream mode: values-------------------")
for chunk in agent.stream(  
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    stream_mode="values", ## or updates
):
    print(f"chunk: {chunk['messages'][-1].pretty_print()}")