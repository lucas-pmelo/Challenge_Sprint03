class Cliente:
    def __init__(self, nome, cpf, email, telefone, endereco, cidade, estado, cep, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.data_nascimento = data_nascimento
        self.bikes = []

    def setId(self, id):
        self.id = id

    def getCpf(self):
        return self.cpf

    def getNome(self):
        return self.nome

    def transformar_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
            "data_nascimento": self.data_nascimento,
            "bikes": self.bikes
        }


class Bike:
    def __init__(self, marca, modelo, valor, ano, cor, n_serie, foto, foto_validada):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.ano = ano
        self.cor = cor
        self.n_serie = n_serie
        self.foto = foto
        self.foto_validada = foto_validada

    def getModelo(self):
        return self.modelo

    def transformar_dicionario(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "valor": self.valor,
            "ano": self.ano,
            "cor": self.cor,
            "n_serie": self.n_serie,
            "foto": self.foto,
            "foto_validada": self.foto_validada
        }
