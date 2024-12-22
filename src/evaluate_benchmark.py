import pandas as pd
from evaluation.correctness import CorrectnessEvaluator

def main():

    data = pd.read_parquet("hf://datasets/openai/openai_humaneval/openai_humaneval/test-00000-of-00001.parquet")
    data['prediction'] = data['canonical_solution']
    data = data.astype(str)
    evaluator = CorrectnessEvaluator(model="EleutherAI/gpt-j-6B")
    result = []
    data.apply(lambda x: result.append(evaluator.evaluate_response(x['prompt'], x['canonical_solution'], x['prediction'], x['test'])), axis='columns')

    result = pd.DataFrame(result).to_csv("resultado_evaluation.csv", index=False)

if __name__ == "__main__":
    main()