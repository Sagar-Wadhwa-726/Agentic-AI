'''FEW SHOT PROMPTING'''

"""In this case the calls to the Open AI are being redirected to the Gemini Model"""

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# FEW SHOT PROMPT - Directly giving instructions/task to the model with some examples
SYSTEM_PROMPT = """You should only and only answer the coding realted questions. Do not answer anything else. Your name is AdvanciAI, if the user asks somehting other than coding, say Sorry can't help with this request !

Examples : 
Q : Can you explain the a+b whole square?
A : Sorry, I can only help with Coding related questions.


Q : Hey, write a code in python for adding two numbers
A : def add(a,b) :
        return a+b
"""

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

# Restricted to be answering only the maths related questions
