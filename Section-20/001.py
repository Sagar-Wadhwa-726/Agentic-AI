# Building a weather agent - users can ask the weather of a specific place, LLM will figure out what the user is asking for and will make an API call to the weather API. LLM must respond back to the user.
# from openai import OpenAI
import requests
from typing import Optional
from pydantic import BaseModel, Field
from openai import OpenAI
import json

# client = OpenAI(
#     api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
def get_weather(city : str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"🤖 The weather in {city} is {response.text}"
    return f"Something went wrong"

# def main():
#     user_query = input("> ")
#     response = client.chat.completions.create(
#         model="gemini-2.5-flash",
#         messages = [
#             {"role" : "user", "content" : user_query}
#         ]
#     );
#     print(f"🤖: {response.choices[0].message.content}")

# print(get_weather("atlanta"))

# Chain of though prompting - model will be more accurate by thinking for some time, like a humnan thinks before solving a problem. 

# Automating chain of thought so that we don't have to manually update the history
class MyOutputFormat(BaseModel):
    step : str = Field(..., description = "The id of the step, example : PLAN, OUTPUT, TOOL etc")
    content : Optional[str] = Field(None, description="The optional string content")
    tool : Optional[str] = Field(None, description="The ID of the tool to be called")
    input : Optional[str] = Field(None, description="The input params for the tool being called")



client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Map of available tools
available_tools = {
    "get_weather" : get_weather
}

SYSTEM_PROMPT = """
You're an expert AI assistant in resolving user queries using chain of thought. You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps. 
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools
For every tool call wait for the observe step which is the output from the called tool

Rules : 

- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (that can be multiple times), and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format :

{   
    "step" : "START" | "PLAN" | "OUTPUT" | "TOOL",
    "content" : "string", 
    "tool" : "string", 
    "input" : "string"
}

Available tools : 

- get_weather(city : str) : Takes city name as an input string and returns the weather information about the city
- 

Example 1: 
START : Hey, can you solve 2+3 * 5 / 10
PLAN : {"step" : "PLAN", "content" : "Looking at the problem, we should solve this using BODMAS method"}
PLAN : {"step" : "PLAN", "content" : "first we must multiple 3 * 5 which is 15"}
PLAN : {"step" : "PLAN", "content" : "now the new equation is 2 + 15 / 10"}
PLAN : {"step" : "PLAN", "content" : "we must perform divide that is 15 / 10 = 1.5"}
PLAN : {"step" : "PLAN", "content" : "now the new equation is 2 + 1.5"}
PLAN : {"step" : "PLAN", "content" : "now finally let's perform addition for 2 + 1.5 which is 3.5"}
PLAN : {"step" : "PLAN", "content" : "Great, we have solved and finally left with 3.5 as answer"}
PLAN : {"step" : "OUTPUT", "content" : "3.5"}

Example 2: 
START : What is the weather of Delhi?
PLAN : {"step" : "PLAN", "content" : "Seems like the user is interested in getting the weather of Delhi, India"}
PLAN : {"step" : "PLAN", "content" : "Let's see if we have any available tools from the list of available tools"}
PLAN : {"step" : "PLAN", "content" : "Great! We have get_weather tool available for this query"}
PLAN : {"step" : "PLAN", "content" : "I need to call get_weather tool for Delhi as the input for city parameter"}
PLAN : {"step" : "TOOL", "tool" : "get_weather", "input" : "Delhi"}
PLAN : {"step" : "OBSERVE", "tool" : "get_weather", "output" : "The weather of delhi is cloud with 20 Degrees Celcius}
PLAN : {"step" : "PLAN", "content" : "Great, I have got the weather info about Delhi"}
PLAN : {"step" : "OUTPUT", "content" : "The weather in Delhi is cloudy with about 20 Degrees celcius"}
"""

print("\n\n\n")

message_history = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    }
]

user_query = input("👉 ")

message_history.append({
    "role": "user",
    "content": user_query 
})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={
            "type" : "json_object"
        },
        messages=message_history
    )

    raw_result = (response.choices[0].message.content)
    print(f"here is the raw result result : {raw_result}")
    message_history.append({
        "role" : "assistant",
        "content" : raw_result
    })
    parsed_result = json.loads(raw_result)
    

    if parsed_result.get('step') == 'START' :
        print("🔥 ", parsed_result.get("content"))
        continue

    if parsed_result.get('step') == 'TOOL' :
        tool_to_be_called = parsed_result.get('tool')
        tool_input = parsed_result.get('input')
        print(f"⚒️  {tool_to_be_called}, {tool_input}")

        tool_response = available_tools[tool_to_be_called](tool_input)
        print(f"⛏️: {tool_to_be_called} ({tool_input}) = {tool_response}")
        message_history.append(
            {
                "role": "developer",
                "content" : json.dumps(
                    {"step" : "OBSERVE", "tool" : tool_to_be_called, "input" : tool_input, "output" : tool_response}
                )
            }
        )
        continue

    if parsed_result.get('step') == 'PLAN' :
        print("🧠 ", parsed_result.get("content"))
        continue

    if parsed_result.get('step') == 'OUTPUT' :
        print("🤖 ", parsed_result.get("content"))
        break

print("\n\n\n")