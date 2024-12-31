import os
import maritalk
from models.model import ModelInterface

class MaritacaModel(ModelInterface):
    def __init__(self, model=None):
        self.model = model 
        self.token = os.getenv("MARITACA_API_KEY")
        self.client = maritalk.MariTalk(key=self.token, model=self.model)

    def load_model(self):
        pass

    def get_completion(self, context):
        response = self.client.generate(
            context,
            do_sample=True,
            max_tokens=1500,
            temperature=0.0,
            top_p=0.95
        )
        return response["answer"]
