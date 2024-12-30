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

- `-m`: Esse parâmetro define os modelos que será utilizado na validação.

Abaixo, apresentamos exemplos de execução dos extratores com auxilílio dos parâmetros de execução:

```bash
python3 evaluate_benchmark.py -m huggingface:meta-llama/Llama-3.2-3B-Instruct
```
