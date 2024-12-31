def evaluation_parser(eval_response):
    import json
    try:
        return eval_response
    except json.JSONDecodeError as e:
        print(f"Erro ao interpretar JSON: {e}")
        raise ValueError("Resposta inválida ou mal formatada")
