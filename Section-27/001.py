# Graph gives relationships about the various data being stored which is not in the case of vector databases
from mem0 import Memory
from openai import OpenAI
import os
import json

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO_CONNECTION_URI = os.getenv("NEO_CONNECTION_URI")
NEO_USERNAME = os.getenv("NEO_USERNAME")
NEO_PASSWORD = os.getenv("NEO_PASSWORD")

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
    },
    "graph_store" : {
        "provider" : "neo4j",
        "config" : {
            "url" : NEO_CONNECTION_URI,
            "username" : NEO_USERNAME,
            "password" : NEO_PASSWORD
        }
    }
}
mem_client = Memory.from_config(config)

while True:
    user_query = input("> ")

    search_memory = mem_client.search(query=user_query, user_id = "sagarwadhwa")

    memories = [
        print(f"ID: {mem.get("id")}\nMemory : {mem.get("memory")}") for mem in search_memory.get("results")
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
    print("Memory Saved . . . ")