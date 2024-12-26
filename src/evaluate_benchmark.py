import pandas as pd
from evaluation.correctness import CorrectnessEvaluator
import os
import argparse
from dotenv import load_dotenv


def parse_parameters() -> dict:
    load_dotenv()
    parser = argparse.ArgumentParser(
        description=""
    )

    parser.add_argument(
        "-m",
        "--models",
        type=str,
        nargs="+",
        help="Path to the models that will be used in the evaluation.",
        default=None,
    )
  
    parser = parser.parse_args()
    params = {
        "models": parser.models,
        "public_key": os.getenv("LANGFUSE_PUBLIC_KEY", None),
    }
    return params


def main():
    data = pd.read_parquet("hf://datasets/openai/openai_humaneval/openai_humaneval/test-00000-of-00001.parquet")
    data['prediction'] = data['canonical_solution']
    data = data.astype(str)
    params = parse_parameters()
    evaluator = CorrectnessEvaluator(params=params)
    result = []
    data.apply(lambda x: result.append(evaluator.evaluate_response(x['prompt'], x['canonical_solution'], x['prediction'], x['test'])), axis='columns')

    result = pd.DataFrame(result).to_csv("resultado_evaluation.csv", index=False)

main()