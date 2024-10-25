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
    m_respostas: list = get_close_matches(pergunta_usuario, perguntas, n=1, cutoff= 0.6)
    return m_respostas[0] if m_respostas else None


def responder(pergunta: str, BancoDeDados: dict) -> str | None:
    for i in BancoDeDados["questions"]:
        if i["question"] == pergunta:
            return i["answer"]
        
def chatbot():
    BancoDeDados: dict = carregar_BD("BancoDeDados.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "sair":
            break

        best_response: str | None = melhor_resposta(user_input, [i["question"] for i in BancoDeDados["questions"]])

        if best_response:
            answer: str = responder(best_response, BancoDeDados)
            print(f"Bot: {answer}")
        else:
            print("Bot: Não Sei como responder a isso, pode me ensinar?")
            nova_resposta: str = input("digite a resposta para a pergunta ou 'pular': ")

            if nova_resposta != "pular":
                BancoDeDados["questions"].append({"question": user_input, "answer": nova_resposta})
                salvar_BD("BancoDeDados.json", BancoDeDados)

                print("Bot: Obrigado por me ensinar!!")

if __name__ == "__main__":
    chatbot()