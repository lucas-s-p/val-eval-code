from models.openai import OpenAIModel
from models.hugging_face import HuggingFaceModel
from models.maritaca import MaritacaModel
from models.groq import GroqModel


class ModelFactory:
    _models = {}

    @staticmethod
    def register_model(name, model_class):
        ModelFactory._models[name] = model_class

    @staticmethod
    def get_model(name, **kwargs):
        model_class = ModelFactory._models.get(name)
        if not model_class:
            raise ValueError(f"Model '{name}' is not registered.")
        return model_class(**kwargs)

# Register the models:
ModelFactory.register_model("openai", OpenAIModel)
ModelFactory.register_model("huggingface", HuggingFaceModel)
ModelFactory.register_model("maritaca", MaritacaModel)
ModelFactory.register_model("groq", GroqModel)