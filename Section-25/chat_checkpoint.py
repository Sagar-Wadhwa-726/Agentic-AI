from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {
        "messages" : [response]
    }

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

def compile_graph_with_checkpointer(checkpointer):
    # graph now compiled having a checkpointer in the Mongo DB database
    return graph_builder.compile(checkpointer=checkpointer)
    
DB_URI = "mongodb://admin:admin@localhost:27017"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    # state is not global, it is associated with a id, store the state corresponding to the id
    config = {
        "configurable" : {
            "thread_id" : "sagar"
        }
    }
    graph_with_checkpoint = compile_graph_with_checkpointer(checkpointer)
    for chunk in graph_with_checkpoint.stream(State({"messages" : ["what is my name?"]}), config=config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()


# Checkpointer (sagar) -> Hey, my name is sagar wadhwa