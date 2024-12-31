from huggingface_hub import InferenceClient

import os
from models.model import ModelInterface

class HuggingFaceModel(ModelInterface):
    def __init__(self, model=None):
        self.model = model
        self.token = os.getenv("HUGGING_FACE_KEY")
        self.client = None

    def load_model(self):
        self.client = InferenceClient(model=self.model, token=self.token)

    def get_completion(self, context):
        context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in context])
        print(context)
        response = self.client.text_generation(prompt=context, max_new_tokens=1500)
        return response
