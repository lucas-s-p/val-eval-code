from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def load_model(self):
        """Carrega o modelo."""
        pass

    @abstractmethod
    def get_completion(self, input_data):
        """Executa a entrada no modelo."""
        pass
