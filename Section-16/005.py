# Chain of though prompting - model will be more accurate by thinking for some time, like a humnan thinks before solving a problem. 
# this approach requires manually adding the history, this will be automated in the next file

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

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    reasoning_effort="low",
    response_format={
        "type" : "json_object"
    },
    messages=[
        {
            # System prompt
            "role" : "system",
            "content" : SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Write a code in python which calls the Open AI api"
        },
        # to keep the history
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "PLAN",
                    "content": "The user wants a Python code example to call the OpenAI API. I need to provide a complete and runnable code snippet."
                }
            )
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "role": "assistant",
                    "content": json.dumps(
                        {
                            "step": "PLAN",
                            "content": "I should first mention the prerequisites, specifically installing the 'openai' library and setting up the API key."
                        }
                    )
                }
            )
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "role": "assistant",
                    "content": json.dumps(
                        {
                            "step": "PLAN",
                            "content": "Next, I will outline the basic structure of the Python code, including importing the library, setting the API key, and making a call to a specific OpenAI model (e.g., for chat completions)."
                        }
                    )
                }
            )
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "role": "assistant",
                    "content": json.dumps(
                        {
                            "step": "PLAN",
                            "content": "I will then provide the Python code snippet, including comments to explain each part. This will involve using `openai.OpenAI()` client, specifying the model, and crafting a `messages` array for chat completions."
                        }
                    )
                }
            )
        },
    ]
)
print(response.choices[0].message.content)
