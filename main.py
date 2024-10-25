import json
from difflib import get_close_matches

def carregar_BD(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def salvar_BD(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def melhor_resposta(pergunta_usuario: str, perguntas: list[str]) -> str | None:
    m_respostas: list = get_close_matches(pergunta_usuario, perguntas, n=1, cutoff=0.6)
    return m_respostas[0] if m_respostas else None

def responder(pergunta: str, BancoDeDados: dict) -> str | None:
    for i in BancoDeDados["questions"]:
        if i["question"].lower() == pergunta.lower():
            return i["answer"]

def chatbot(user_input: str) -> dict:
    BancoDeDados = carregar_BD("BancoDeDados.json")
    best_response = melhor_resposta(user_input, [i["question"] for i in BancoDeDados["questions"]])

    if best_response:
        answer = responder(best_response, BancoDeDados)
        return {"answer": answer, "known": True}
    else:
        return {"answer": "Não sei como responder a isso, pode me ensinar?", "known": False}

def adicionar_pergunta_resposta(pergunta: str, resposta: str):
    BancoDeDados = carregar_BD("BancoDeDados.json")
    BancoDeDados["questions"].append({"question": pergunta, "answer": resposta})
    salvar_BD("BancoDeDados.json", BancoDeDados)
