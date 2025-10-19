# Custom Tokenizer
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-5")

text = "Hey there ! My name is Sagar Wadhwa"

# [25216, 1354, 1073, 3673, 1308, 382, 336, 23482, 486, 7422, 1708]
tokens = encoder.encode(text)
print(tokens)

# Hey there ! My name is Sagar Wadhwa
decoded_text = encoder.decode(tokens)
print(decoded_text)


