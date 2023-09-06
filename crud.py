from models import Cliente, Bike
from functions import get_float, get_int, verificar_bike, sair, verificar_n_serie
from db import *


def cadastrar_cliente(cpf):
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = get_int("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    estado = input("Digite o estado do cliente: ")
    cep = get_int("Digite o CEP do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente: ")
    cliente = Cliente(
        nome,
        cpf,
        email,
        telefone,
        endereco,
        cidade,
        estado,
        cep,
        data_nascimento
    )
    escrever_cliente(cliente)
    return cliente


def cadastrar_bike(cliente):
    print("Agora, vamos precisar de uma foto da bike e o número de série e uma foto para validar o cadastro dela!")

    verificacao_n_serie = verificar_n_serie()
    if not verificacao_n_serie[1]:
        sair()

    verificacao_bike = verificar_bike()
    if not verificacao_bike:
        sair()

    print("Tudo certo com as fotos! Vamos continuar o cadastro da Bike!")

    marca = input("Digite a marca da bike: ")
    modelo = input("Digite o modelo da bike: ")
    valor = get_float("Digite o valor da bike: ")
    ano = get_int("Digite o ano da bike: ")
    cor = input("Digite a cor da bike: ")
    bike = Bike(
        marca,
        modelo,
        valor,
        ano,
        cor,
        verificacao_n_serie[0],
        foto=verificacao_n_serie[1],
        foto_validada=verificacao_bike
    )
    adicionar_bike(cliente, bike)
    return bike


def mostrar_clientes():
    clientes = buscar_todos_clientes()

    if clientes == []:
        print("Não há clientes cadastrados")
        return

    for cliente in clientes:
        print(f"\nNome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}\n")
        if cliente['bikes'] == []:
            print("Não há bikes cadastradas")
            continue

        print("Bikes: ")
        for bike in cliente['bikes']:
            print(f" -Modelo: {bike['modelo']}")
            print(f" -Ano: {bike['ano']}")
            print(f" -N° de série: {bike['n_serie']}\n")
