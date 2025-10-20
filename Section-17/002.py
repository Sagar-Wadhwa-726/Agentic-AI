"""

# Alpaca style prompt - used by alpaca llama model, it goes on like this:

### Instruction: <SYSTEM_PROMPT>\n
### Input: <USER_PROMPT>\n
### Response: \n

# ChatML schema / ChatML type prompting - this has been used before (in open ai/ gemini api calls)

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

# INST (Instruction) prompting - used by llama-2 models

[INST] What is the time now ? [/INST]


"""
