
class Conta:

    # Construtor
    def __init__(self, numero, titular, saldo, limite= 1000.0):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # aula 3
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    # aula 3
    def deposita(self, valor):
        print(f"Valor depositado {valor}")
        self.saldo += valor

    # aula 3
    def saca(self, valor):
        print(f"Valor sacado {valor}")
        self.saldo -= valor