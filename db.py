from models import *
import os
import json


NOME_ARQUIVO = "db/clientes.json"


def inicializar():
    arquivo = open(NOME_ARQUIVO, "a")
    isempty = os.stat(NOME_ARQUIVO).st_size == 0
    if isempty:
        conteudo = {
            "clientes": []
        }

        arquivo.write(json.dumps(conteudo))
    arquivo.close()


def escrever_cliente(cliente):
    arquivo_cliente = open(NOME_ARQUIVO, "r")
    conteudo = json.load(arquivo_cliente)

    if len(conteudo["clientes"]) == 0:
        cliente.setId(1)
    else:
        cliente.setId(conteudo["clientes"][-1]["id"] + 1)

    conteudo["clientes"].append(cliente.transformar_dicionario())

    arquivo_cliente = open(NOME_ARQUIVO, "w")
    arquivo_cliente.write(json.dumps(conteudo))

    arquivo_cliente.close()


def buscar_cliente(cpf):
    arquivo_cliente = open(NOME_ARQUIVO, "r")
    conteudo = json.load(arquivo_cliente)

    for cliente in conteudo["clientes"]:
        if cliente["cpf"] == cpf:
            del cliente["id"]
            del cliente["bikes"]
            return Cliente(**cliente)


def adicionar_bike(cliente, bike):
    arquivo_cliente = open(NOME_ARQUIVO, "r")
    conteudo = json.load(arquivo_cliente)
    for cliente_conteudo in conteudo["clientes"]:
        if cliente_conteudo["cpf"] == cliente.getCpf():
            cliente_conteudo["bikes"].append(bike.transformar_dicionario())
            break

    arquivo_cliente = open(NOME_ARQUIVO, "w")
    arquivo_cliente.write(json.dumps(conteudo))

    arquivo_cliente.close()


def buscar_todos_clientes():
    arquivo_cliente = open(NOME_ARQUIVO, "r")
    conteudo = json.load(arquivo_cliente)
    return conteudo["clientes"]


inicializar()
