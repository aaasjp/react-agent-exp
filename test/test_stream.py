from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
  topic: str
  joke: str


def refine_topic(state: State):
    return {"topic": state["topic"] + " and cats"}


def generate_joke(state: State):
    return {"joke": f"This is a joke about {state['topic']}"}

graph = (
  StateGraph(State)
  .add_node(refine_topic)
  .add_node(generate_joke)
  .add_edge(START, "refine_topic")
  .add_edge("refine_topic", "generate_joke")
  .add_edge("generate_joke", END)
  .compile()
)

print("-------------stream mode: updates-------------------")
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode="updates",  
):
    print(chunk)


print("-------------stream mode: values-------------------")
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode="values",  
):
    print(chunk)


'''
-------------stream mode: updates-------------------
{'refine_topic': {'topic': 'ice cream and cats'}}
{'generate_joke': {'joke': 'This is a joke about ice cream and cats'}}
-------------stream mode: values-------------------
{'topic': 'ice cream'}
{'topic': 'ice cream and cats'}
{'topic': 'ice cream and cats', 'joke': 'This is a joke about ice cream and cats'}
'''