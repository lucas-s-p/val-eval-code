from evaluation.prompts import default_user_prompt, benchmark_evaluation_system_prompt
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
        
        list_response = []
        for model_spec in self.params['models']:
            try:
                api, model_path = model_spec.split(":", 1)
                model_instance = ModelFactory.get_model(api, model=model_path)
                model_instance.load_model()
                
                eval_response = model_instance.get_completion(messages)
                list_response.append(eval_response)
            except Exception as e:
                print(f"Error processing model '{model_spec}': {e}")
        
        print(list_response)

        return {
            'prompt': input,
            'reference': reference,
            'prediction': prediction,
            'test': tests,
            'evaluation': list_response,
        }
