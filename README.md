# VAL-EVAL-CODE

## Gerenciamento de dependências

Para a instalação das dependências, execute o seguinte comando:
```bash
pip install -r requirements.txt
```

## Variáveis de ambiente

Faça uma cópia do arquivo `.env.example`, renomeie-o como `.env` e preencha-o com os valores das variáveis de ambiente.

## Parâmetros de execução

No terminal, você pode utilizar parâmetros para personalizar a validção dos resultados. Os parâmetros disponíveis são:

- **`-m`**  
  Especifica o modelo a ser utilizado na validação. Deve ser informado no formato aceito pela ferramenta (e.g., `huggingface:meta-llama/Llama-2-7b-hf`).  

- **`-d`**  
  Define o caminho para o dataset a ser utilizado na validação. O arquivo pode estar nos formatos `.parquet` ou `.csv`.  

- **`-p`**  
  Indica o nome da coluna no dataset que contém os valores de entrada (`input`) das instâncias.  

- **`-r`**  
  Define o nome da coluna no dataset que contém as respostas de referência (`reference`) esperadas para as instâncias.  

- **`-t`**  
  Especifica o nome da coluna no dataset que contém os resultados dos testes (`tests`) já aplicados às instâncias.  

Abaixo, apresento exemplos de execução dos extratores com auxilílio dos parâmetros de execução:

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
```
