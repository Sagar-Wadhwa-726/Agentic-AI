from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

# Ollama running on this URL
client = Client(
    host="http://localhost:11434",
)

@app.post("/chat")
def chat(message: str = Body(..., description="The message")):
    response = client.chat(model="gemma2:2b", messages=[
        {
            "role" : "user",
            "content" : message
        }
    ])
    return {"response" : response.message.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)