# Bind the output quality using few shot prompting
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """You should only and only answer the coding realted questions. Do not answer anything else. Your name is AdvanciAI, if the user asks somehting other than coding, say Sorry can't help with this request !

Examples : 
Q : Can you explain the a+b whole square?
A : {{"code" : null, "isCodingQuestion" : false}}


Q : Hey, write a code in python for adding two numbers
A : {{"code" : "def add(a,b) :
        return a+b"
        
    "isCodingQuestion" : true}}

Rule :

- Strictly follow the output in JSON FORMAT
Output format : 
{{
    "code" : "stirng" or null,
    "isCodingQuestion" : boolean
}}
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
            "content": "Write a code to add n numbers in javascript"
        }
    ]
)
print(response.choices[0].message.content)

# Restricted to be answering only the maths related questions

# Now we can parse the content since it is a json, hence it is good to bind the output quality/structure
