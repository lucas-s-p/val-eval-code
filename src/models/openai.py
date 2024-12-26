import os
from openai import OpenAI
from dotenv import load_dotenv

from models.model import ModelInterface

class OpenAIModel(ModelInterface):
    def __init__(self):
        load_dotenv()
        self.client = None

    def load_model(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_completion(self, messages, model=None):
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=model,
        )
        return chat_completion.choices[0].message.content
