import time
from crud import cadastrar_cliente, cadastrar_bike, mostrar_clientes
from functions import limpar_tela, menu_principal, sair, get_escolha, get_int, print_sleep
from db import *


def vistoria_completa():
    limpar_tela()
    print_sleep("Para começarmos, vamos cadastrar o cliente!", 3)

    cliente = opcao_cadastrar_cliente()

    limpar_tela()

    escolha_cadastro_bike = get_escolha("Deseja cadastrar uma bike? [S/N]: ")
    if not escolha_cadastro_bike:
        sair()

    opcao_cadastrar_bike(cliente)

    sair()


def opcao_cadastrar_cliente():
    limpar_tela()
    cpf = get_int("Digite o CPF do cliente: ")
    cliente = buscar_cliente(cpf)

    if cliente:
        print_sleep("Cliente já cadastrado!", 3)
    else:
        cliente = cadastrar_cliente(cpf)
        print_sleep(
            f"\nCliente {cliente.nome}, foi cadastrado(a) com sucesso!", 3)

    return cliente


def opcao_cadastrar_bike(cliente=None):
    if not cliente:
        while True:
            cpf = get_int("Digite o seu CPF: ")
            cliente = buscar_cliente(cpf)
            if not cliente:
                print_sleep("Cliente não encontrado! Tente novamente", 3)
                limpar_tela()
            else:
                break

    print_sleep(f"Olá, {cliente.getNome()}!", 2)
    while True:
        limpar_tela()
        bike = cadastrar_bike(cliente)
        print_sleep(f"\nA bike {bike.modelo}, foi cadastrada com sucesso!", 3)

        cadastrar_novamente = get_escolha(
            "Deseja cadastrar outra bike? [S/N]: ")
        if not cadastrar_novamente:
            break


def opcao_mostrar_clientes():
    mostrar_clientes()
    input("Pressione Enter para continuar...")
    limpar_tela()


def main():
    while True:
        print("\nBem vindo ao sistema de vistoria de seguro de bike!\n")
        opcao = menu_principal()

        match opcao:
            case 1:
                vistoria_completa()
                break
            case 2:
                opcao_cadastrar_bike()
                break
            case 3:
                opcao_mostrar_clientes()
            case 4:
                sair()
            case _:
                print("Opção inválida")
                time.sleep(3)
                limpar_tela()


main()
