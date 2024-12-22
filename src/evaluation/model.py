import os

from huggingface_hub import InferenceClient

client = InferenceClient(model="EleutherAI/gpt-j-6B", token="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")

def get_completion(context, model="EleutherAI/gpt-j-6B"):
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in context])
    print(context)
    response = client.text_generation(prompt=context, max_new_tokens=150)
    return response

'''
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY", None)
)

def get_completion(messages, model="gpt-3.5-turbo"):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return chat_completion.choices[0].message.content
'''