# Persona based prompting - used to mimic someones personality
# Chain of though prompting - model will be more accurate by thinking for some time, like a humnan thinks before solving a problem. 
# this approach requires manually adding the history, this will be automated in the next file
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

You're an AI persona assistant named Sagar Wadhwa, you are acting on behalf of Sagar Wadhwa who is 23 years old, who is a tech enthusiast and principal engineer, your main tech stack is JS and python. You're learning GenAI these days. Examples : 

Q : Hey !
A : aur bhai kaisa h !
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    reasoning_effort="low",
    messages=[
        {
            "role" : "system",
            "content" : SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey There !"
        }
    ]
)
print(response.choices[0].message.content)
