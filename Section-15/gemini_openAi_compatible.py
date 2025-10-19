"""In this case the calls to the Open AI are being redirected to the Gemini Model"""

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
            "role": "user",
            "content": "Just tell me which model you are?"
        }
    ]
)
print(response.choices[0].message.content)