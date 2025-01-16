# VAL-EVAL-CODE (Code Evaluation Validator)

## Dependency Management

To install the dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Environment Variables

Make a copy of the `.env.example` file, rename it to `.env`, and fill it with the appropriate environment variable values.

## Dataset with Predictions

Make a copy of the `prediction.csv.example` file, rename it to `prediction.csv`, and add the benchmark predictions to the file.

## Execution Parameters

In the terminal, you can use parameters to customize the validation of results. The available parameters are:

- **`-m`**  
  Specifies the model to be used in the validation. It must be provided in a format accepted by the tool (e.g., `huggingface:meta-llama/Llama-2-7b-hf`).  

- **`-d`**  
  Defines the path to the dataset to be used in the validation. The file can be in `.parquet` or `.csv` formats.  

- **`-p`**  
  Indicates the name of the column in the dataset that contains the input values (`input`) of the instances.  

- **`-r`**  
  Defines the name of the column in the dataset that contains the expected reference responses (`reference`) for the instances.  

- **`-t`**  
  Specifies the name of the column in the dataset that contains the test results (`tests`) already applied to the instances.  

Below are examples of running the extractors with the help of the execution parameters:

```bash
python3 evaluate_benchmark.py \
    --models huggingface:meta-llama/Llama-3.2-3B-Instruct \
    --dataset "hf://datasets/openai/openai_humaneval/openai_humaneval/test-00000-of-00001.parquet" \
    --prompt_col "prompt" \
    --reference_col "canonical_solution" \
    --test_suite_col "test"

python3 evaluate_benchmark.py \
    -m maritaca:sabia-2-small \
    --dataset "hf://datasets/openai/openai_humaneval/openai_humaneval/test-00000-of-00001.parquet" \
    --prompt_col "prompt" \
    --reference_col "canonical_solution" \
    --test_suite_col "test"

python3 evaluate_benchmark.py \
    -m groq:llama-3.3-70b-versatile \
    --dataset "hf://datasets/openai/openai_humaneval/openai_humaneval/test-00000-of-00001.parquet" \
    --prompt_col "prompt" \
    --reference_col "canonical_solution" \
    --test_suite_col "test"
