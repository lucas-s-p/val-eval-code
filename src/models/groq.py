import os
from groq import Groq
from models.model import ModelInterface

class GroqModel(ModelInterface):
    def __init__(self, model=None):
        self.model = model
        self.token = os.getenv("GROK_API_KEY")
        self.client = Groq(api_key=self.token)

    def load_model(self):
        pass

    def get_completion(self, context):
        response = self.client.chat.completions.create(
            messages=context,
            model=self.model
        )
        return response.choices[0].message.content
