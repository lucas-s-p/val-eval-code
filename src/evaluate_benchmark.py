import pandas as pd
from evaluation.processor import CorrectnessEvaluator
from dataset.dataset import DatasetLoader
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

    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        help="",
        default=None,
    )
    
    parser.add_argument(
        "-p",
        "--prompt_col",
        type=str,
        help="",
        default=None,
    )
    
    parser.add_argument(
        "-r",
        "--reference_col",
        type=str,
        help="",
        default=None,
    )

    parser.add_argument(
        "-t",
        "--test_suite_col",
        type=str,
        help="",
        default=None,
    )

    parser = parser.parse_args()
    params = {
        "models": parser.models,
        "dataset": parser.dataset,
        "prompt_col": parser.prompt_col,
        "reference_col": parser.reference_col,
        "test_suite_col": parser.test_suite_col,
    }
    return params


def main():
    params = parse_parameters()
    evaluator = CorrectnessEvaluator(params=params)

    #data = pd.read_parquet("hf://datasets/openai/openai_humaneval/openai_humaneval/test-00000-of-00001.parquet")
    dataset = DatasetLoader(params=params)
    data = dataset.load()
    data['prediction'] = data['canonical_solution']
    data = data.astype(str)

    result = []
    data.apply(lambda row: result.append(evaluator.evaluate_response(row[params['prompt_col']], row[params['reference_col']], row['prediction'], row[params['test_suite_col']])), axis='columns')

    result = pd.DataFrame(result).to_csv("resultado_evaluation.csv", index=False)

main()