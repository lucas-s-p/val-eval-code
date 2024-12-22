from evaluation.prompts import default_user_prompt, benchmark_evaluation_system_prompt
from evaluation.utils import evaluation_parser
from evaluation.model import get_completion


class CorrectnessEvaluator:
    def __init__(self, model):
        self.model = model
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
        
        eval_response = get_completion(messages, self.model)
        evaluation = evaluation_parser(eval_response)

        return {
            'prompt': input,
            'reference': reference,
            'prediction': prediction,
            'test': tests,
            'evaluation': evaluation,
        }
