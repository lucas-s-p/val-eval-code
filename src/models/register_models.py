from models.gpt import OpenAIModel
from models.neo_gpt import HuggingFaceModel


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

# Registre os modelos
ModelFactory.register_model("openai", OpenAIModel)
ModelFactory.register_model("neo_gpt", HuggingFaceModel)