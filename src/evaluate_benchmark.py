import pandas as pd
import argparse
from evaluation.processor import CorrectnessEvaluator
from dataset.dataset import DatasetLoader
from dotenv import load_dotenv
from evaluation.performance_calculator import PerformanceCalculator
from tqdm import tqdm


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
        help="",
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
    parser.add_argument(
        "-l",
        "--lang_prompt",
        type=str,
        help="",
        default='pt'
    )

    parser = parser.parse_args()
    params = {
        "models": parser.models,
        "dataset": parser.dataset,
        "prompt_col": parser.prompt_col,
        "reference_col": parser.reference_col,
        "test_suite_col": parser.test_suite_col,
        "lang_prompt": parser.lang_prompt
    }
    return params


def main():
    try:
        params = parse_parameters()
        evaluator = CorrectnessEvaluator(params=params)

        dataset = DatasetLoader(params=params)
        data = dataset.load()

        tqdm.pandas(desc="Progress", ncols=90)
        
        result = []
        data.progress_apply(lambda row: result.append(evaluator.evaluate_response(row[params['prompt_col']], row[params['reference_col']], row['prediction'], row[params['test_suite_col']])), axis='columns')

        result = pd.DataFrame(result)
        result.to_csv("result_evaluation.csv", index=False)
        efficiency = PerformanceCalculator.calculate(result['evaluation'], params['lang_prompt'])
        print("The accuracy obtained is:", round(efficiency,2), "%")
    except Exception as e:
        print(f"Error while running the script: {e}")

main()