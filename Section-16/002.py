'''ZERO SHOT PROMPTING'''

"""In this case the calls to the Open AI are being redirected to the Gemini Model"""
# Here we are giving some context, that the bot is now just answering maths related questions
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ZERO SHOT PROMPT - Directly giving instructions/task to the model without prior examples
SYSTEM_PROMPT = "You should only and only answer the coding realted questions. Do not answer anything else. Your name is AdvanciAI, if the user asks somehting other than coding, say Sorry can't help with this request !"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    reasoning_effort="low",
    messages=[
        {
            # System prompt
            "role" : "system",
            "content" : SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "tell me a joke"
        }
    ]
)
print(response.choices[0].message.content)
