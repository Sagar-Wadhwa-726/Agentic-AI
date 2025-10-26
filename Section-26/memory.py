from mem0 import Memory
from openai import OpenAI
import os
import json

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()

config = {
    "version" : "v1.1",
    "embdder" : {
        "provider" : "openai",
        "config" : {
            "api_key" : OPENAI_API_KEY,
            "model" : "text-embedding-3-small"
        }
    },
    "llm" : {
        "provider" : "openai",
        "config" : {
            "api_key" : OPENAI_API_KEY,
            "model" : "gpt-4.1"
        }
    },
    "vector_store" : {
        "provider" : "qdrant",
        "config" : {
            "host" : "localhost",
            "port" : 6333
        }
    }
}

# this gives a memory client
mem_client = Memory.from_config(config)

# we have to chat with the model and give every chat model to the memory client

while True:
    user_query = input("> ")

    search_memory = mem_client.search(query=user_query, user_id = "sagarwadhwa")

    memories = [
        f"ID: {mem.get("id")}\nMemory : {mem.get("memory")}" for mem in search_memory.get("results")
    ]

    SYSTEM_PROMPT = f"""

        Here is the context about the user : 
        {json.dumps(memories)}


    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content
    print("AI: ", ai_response)

    mem_client.add(
        user_id = "sagarwadhwa",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    # mem0 will automatically decide what needs to be stored in the short term memory, what needs to be stored in the long term memory - as in semantic memory, episodic memory, and factual memory, we don't have to decide anything here
    print("Memory Saved . . . ")