from transformers import pipeline

# This will download the model and run it locally, won't run this and hence commented since the model is going to be huge and not possible to run on the local machine

# pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")
# messages = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
#             {"type": "text", "text": "What animal is on the candy?"}
#         ]
#     },
# ]
# pipe(text=messages)