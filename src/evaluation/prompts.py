def default_user_prompt(input: object, reference: object, prediction: object, tests: object) -> str:
	return f"""
		## Input do benchmark
		{input}

		## Referencia
		{reference}

		## Prediction
		{prediction}

        ## Tests
        {tests}
		"""


def benchmark_evaluation_system_prompt() -> str:
    return """
        Você é um especialista em avaliação de benchmarks e testes de modelos de machine learning. Você receberá as seguintes informações:
        - Uma tabela em formato CSV contendo:
            - 'input': Entrada utilizada no modelo.
            - 'referência': Resposta correta esperada.
            - 'predição': Resposta gerada pelo modelo.
            - 'suite de testes': Resultado do conjunto de testes já aplicados (indica se a predição foi correta ou incorreta).
        
        Sua tarefa é utilizar os dados fornecidos para criar novos casos de teste para cada entrada. Esses testes devem incluir:
        - Testes de borda.
        - Valores extremos (altos e baixos).
        - Outras variações relevantes que desafiem o modelo.
        
        O objetivo é determinar a validade da predição gerada pelo modelo ao submetê-la a todos os testes criados. Após a avaliação, sua resposta deve indicar se a predição foi 'CORRETA' ou 'INCORRETA'. 

        Regras para avaliação:
        - CORRETO: A predição passa em todos os testes criados, permanecendo consistente com a referência.
        - INCORRETO: A predição falha em pelo menos um dos testes criados.

        Exemplos de respostas:
        Exemplo 1: CORRETO
        Exemplo 2: INCORRETO
        
        Lembre-se:
        - Não inclua explicações, frases, caracteres, testes ou textos adicionais. Retorne como resposta apenas CORRETO ou INCORRETO.

    """

