from evaluation.prompts import default_user_prompt, benchmark_evaluation_system_prompt
from evaluation.utils import evaluation_parser
from models.model import ModelInterface
from models.register_models import ModelFactory


class CorrectnessEvaluator:
    def __init__(self, params={}):
        self.params = params
        self.correctness_prompt = benchmark_evaluation_system_prompt()

    def evaluate_response(self, input, reference, prediction, tests):
        
        if input is None or reference is None:
            raise ValueError("message and response must be provided")
        
        messages = [
            {
                'role': "system",
                'content': self.correctness_prompt
            },
            {
                'role': "user",
                'content': default_user_prompt(input, reference, prediction, tests)
            }
        ]
        
        for model_name in self.params['models']:
            try:
                # Criar a instância do modelo usando a fábrica
                model_instance = ModelFactory.get_model(model_name)
                
                # Carregar o modelo (se necessário)
                model_instance.load_model()
                
                # Executar o método get_completion
                eval_response = model_instance.get_completion(messages)
                print(eval_response)
                # Processar a resposta
                evaluation = evaluation_parser(eval_response)
                
            except Exception as e:
                print(f"Error processing model '{model_name}': {e}")


        return {
            'prompt': input,
            'reference': reference,
            'prediction': prediction,
            'test': tests,
            'evaluation': evaluation,
        }
