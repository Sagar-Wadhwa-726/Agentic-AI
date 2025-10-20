# Chain of though prompting - model will be more accurate by thinking for some time, like a humnan thinks before solving a problem. 

# Automating chain of thought so that we don't have to manually update the history

from openai import OpenAI
import json

client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

You're an expert AI assistant in resolving user queries using chain of thought. You work on START, PLAN and OUTPUT steps.

You need to first PLAN what needs to be done. The PLAN can be multiple steps. 

Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules : 

- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (that can be multiple times), and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format :

{"step" : "START" | "PLAN" | "OUTPUT", "content" : "string}

Example : 
START : Hey, can you solve 2+3 * 5 / 10
PLAN : {"step" : "PLAN", "content" : "Looking at the problem, we should solve this using BODMAS method"}
PLAN : {"step" : "PLAN", "content" : "first we must multiple 3 * 5 which is 15"}
PLAN : {"step" : "PLAN", "content" : "now the new equation is 2 + 15 / 10"}
PLAN : {"step" : "PLAN", "content" : "we must perform divide that is 15 / 10 = 1.5"}
PLAN : {"step" : "PLAN", "content" : "now the new equation is 2 + 1.5"}
PLAN : {"step" : "PLAN", "content" : "now finally let's perform addition for 2 + 1.5 which is 3.5"}
PLAN : {"step" : "PLAN", "content" : "Great, we have solved and finally left with 3.5 as answer"}
PLAN : {"step" : "OUTPUT", "content" : "3.5"}
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
    message_history.append({
        "role" : "assistant",
        "content" : raw_result
    })
    parsed_result = json.loads(raw_result)

    if parsed_result.get('step') == 'START' :
        print("🔥 ", parsed_result.get("content"))
        continue

    if parsed_result.get('step') == 'PLAN' :
        print("🧠 ", parsed_result.get("content"))
        continue

    if parsed_result.get('step') == 'OUTPUT' :
        print("🤖 ", parsed_result.get("content"))
        break

print("\n\n\n")