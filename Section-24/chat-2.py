from dotenv import load_dotenv
load_dotenv()

from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from openai import OpenAI

client = OpenAI()

class State(TypedDict):
    user_query: str
    llm_output : Optional[str]
    is_good : Optional[bool]


def chatbot(state: State):
    print("Inside chatbot node ", state)
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {"role" : "user", "content" : state.get("user_query")} 
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: State) -> Literal["chatbot_gemini", "endnode"]:
    print("Inside evaluate_response node ", state)
    # if the evaluation of the response is good, then just return the END
    if True:
        return "endnode"
    # if the evaluation of the response is not good, then specify the other node to be redirected to
    return "chatbot_gemini"
    
def chatbot_gemini(state: State):
    print("Inside chatbot_gemini node ", state)
    response = client.chat.completions.create(
        model = "gpt-4.1",
        messages = [
            {"role" : "user", "content" : state.get("user_query")} 
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state: State):
    print("Inside endnode node ", state)
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("endnode", endnode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode",END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query" : "What is 2+2 ?"}))
print("\n\nUpdated State : ", updated_state)