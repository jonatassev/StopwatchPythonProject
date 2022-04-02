from datetime import date


class Dados():
    def __init__(self, cliente, nome, horas, acao, descricao):
        self.cliente = cliente
        self.nome = nome 
        self.data =  date.today().strftime("%d/%m/%Y")
        self.horas = horas
        self.acao = acao
        self.descricao = descricao