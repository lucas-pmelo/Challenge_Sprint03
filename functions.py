import sys
import time
import os
from reconhecimento_IA import ia_bike as reconhecimento_bike
from reconhecimento_IA import ia_numero_serie as reconhecimento_numero_serie


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def sair():
    limpar_tela()
    print("Obrigado por utilizar o sistema!")
    sys.exit(0)


def get_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Digite um número inteiro\n")


def get_float(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Digite um número inteiro ou decimal\n")


def get_escolha(message):
    while True:
        value = input(message)
        if value.upper() == "S":
            return True
        elif value.upper() == "N":
            return False
        else:
            print("Digite S para sim e N para não\n")


def menu_principal():
    print("1 - Vistoria Completa (Recomendamos essa opção caso queira ter a experiencia de nossos clientes apenas)")
    print("2 - Cadastrar Bike")
    print("3 - Mostrar clientes")
    print("4 - Sair")
    opcao = get_int("Digite a opção desejada: ")
    return opcao


def verifica_existencia_arquivo(path):
    if (os.path.isfile(path)):
        return True
    return False


def verifica_extensao_arquivo(path):
    if (path.endswith(".jpg")):
        return True
    return False


def verificar_bike(tentativa=0):
    tentativa += 1

    while True:
        bike_path = input("Digite o caminho da foto da bike: ")

        if (not verifica_existencia_arquivo(bike_path)):
            print("Arquivo não encontrado!")
            continue

        if (not verifica_extensao_arquivo(bike_path)):
            print("Arquivo não é uma imagem jpg!")
            continue

        break

    reconhecimento = reconhecimento_bike.main(bike_path)

    if reconhecimento:
        print_sleep("Bike validada com sucesso!", 3)
        return bike_path

    print("Bike não reconhecida! Tente novamente")

    print_sleep(f"Tentativas restantes: {3 - tentativa}", 3)

    if tentativa == 3:
        print_sleep(
            "Você excedeu o número de tentativas! Contate nossa central de atendimento!", 5)
        return False

    return verificar_bike(tentativa)


def verificar_n_serie(tentativa=0):
    tentativa += 1

    while True:
        n_serie = input("Digite o número de série da bike: ")
        n_serie_path = input("Digite o caminho da foto do número de série: ")

        if (not verifica_existencia_arquivo(n_serie_path)):
            print("Arquivo não encontrado!")
            continue

        if (not verifica_extensao_arquivo(n_serie_path)):
            print("Arquivo não é uma imagem jpg!")
            continue
        break

    reconhecimento = reconhecimento_numero_serie.main(n_serie_path)

    if reconhecimento == n_serie:
        print_sleep("Número de série validado com sucesso!", 3)
        return [n_serie, n_serie_path]

    print("Número de série não reconhecido! Tente novamente")

    print_sleep(f"Tentativas restantes: {3 - tentativa}", 3)

    if tentativa == 3:
        print_sleep(
            "Você excedeu o número de tentativas! Contate nossa central de atendimento!", 5)
        return [n_serie, False]

    return verificar_n_serie(tentativa)


def print_sleep(texto, tempo):
    print(texto)
    time.sleep(tempo)
