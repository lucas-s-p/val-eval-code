from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def load_model(self):
        """Load the model."""
        pass

    @abstractmethod
    def get_completion(self, input_data):
        """Executes the input to the model."""
        pass
