"""In this case the calls to the Open AI are being redirected to the Gemini Model"""
# Here we are giving some context, that the bot is now just answering maths related questions
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBC7NYzv6WcIOz9kWng9nT7QEKryFYGMQ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    reasoning_effort="low",
    messages=[
        {
            # System prompt
            "role" : "system",
            "content" : "You are an expert in Maths and only and only answer maths related questions. If the query is not realted to maths, just say, sorry I can't help with this request !"
        },
        {
            "role": "user",
            "content": "what is a+b ka whole square jaldi bata !"
        }
    ]
)
print(response.choices[0].message.content)

# Restricted to be answering only the maths related questions
