def evaluation_parser(eval_response):
    import json
    print(f"Resposta recebida: {eval_response}")
    try:
        eval_dict = json.loads(eval_response)
        evaluation = eval_dict['evaluation']
        return evaluation
    except json.JSONDecodeError as e:
        print(f"Erro ao interpretar JSON: {e}")
        raise ValueError("Resposta inválida ou mal formatada")
