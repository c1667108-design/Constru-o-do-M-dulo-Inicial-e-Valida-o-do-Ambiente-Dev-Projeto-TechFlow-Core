"""
TECHFLOW CORE
Sistema de gerenciamento de demandas desenvolvido em Python.
"""
from utils import (
    exibir_titulo,
    validar_prioridade,
    formatar_status
)

# Lista que armazena as demandas
demandas = []

# Controle do próximo ID
proximo_id = 1


# CREATE - Cadastrar demanda
def cadastrar_demanda():
    """Cadastra uma nova demanda no sistema."""
    global proximo_id

    titulo = input("Digite o título: ")
    solicitante = input("Digite o solicitante: ")
    prioridade = input("Digite a prioridade: ")
    while not validar_prioridade(prioridade):
        print("Prioridade inválida! Digite Alta, Média ou Baixa.")
        prioridade = input("Digite a prioridade: ")

    prioridade = prioridade.strip().capitalize()
    cep = input("Digite o CEP: ")
    cidade = input("Digite a cidade: ")

    demanda = {
        "id": proximo_id,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Pendente"
    }

    demandas.append(demanda)
    proximo_id += 1

    print("Demanda cadastrada com sucesso!")


# READ - Listar demandas
def listar_demandas():
    """Exibe todas as demandas cadastradas."""
    if len(demandas) == 0:
        print("Nenhuma demanda cadastrada.")
    else:
        for demanda in demandas:
            print("--------------------")
            print("ID:", demanda["id"])
            print("Título:", demanda["titulo"])
            print("Solicitante:", demanda["solicitante"])
            print("Prioridade:", demanda["prioridade"])
            print("CEP:", demanda["cep"])
            print("Cidade:", demanda["cidade"])
            print("Status:", demanda["status"])


# UPDATE - Atualizar demanda
def atualizar_demanda():
    """Atualiza o status de uma demanda pelo seu ID."""
    try:
        id_busca = int(input("Digite o ID da demanda: "))

        for demanda in demandas:
            if demanda["id"] == id_busca:
                novo_status = input("Digite o novo status: ")
                demanda["status"] = formatar_status(novo_status)

                print("Demanda atualizada!")
                return

        print("Demanda não encontrada.")

    except ValueError:
        print("Digite um ID numérico válido.")


# DELETE - Excluir demanda
def excluir_demanda():
    """Exclui uma demanda cadastrada pelo seu ID."""
    try:
        id_busca = int(input("Digite o ID da demanda: "))

        for demanda in demandas:
            if demanda["id"] == id_busca:
                demandas.remove(demanda)
                print("Demanda excluída!")
                return

        print("Demanda não encontrada.")

    except ValueError:
        print("Digite um ID numérico válido.")


# MENU PRINCIPAL
def menu():
    """Exibe o menu principal e controla as opções do sistema."""
    exibir_titulo("TECHFLOW CORE")
    while True:
        print("\n===== TECHFLOW CORE =====")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Atualizar demanda")
        print("4 - Excluir demanda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            atualizar_demanda()

        elif opcao == "4":
            excluir_demanda()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


# EXECUÇÃO DO SISTEMA
menu()
