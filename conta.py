
class Conta:

    # Construtor
    def __init__(self, numero, titular, saldo, limite= 1000.0):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001" # Aula 6

    # aula 3
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    # aula 3
    def deposita(self, valor):
        self.__saldo += valor

    # Aula 6 - Metodos privado
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    # aula 3
    def saca(self, valor):
        if(self.__pode_sacar(valor)):    #Aula 6 -  Melhorndo o saca
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    # aula 4 - Encapsulamento
    def transfere(self, valor,  conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    # Esse metodo deveria estar na classe de cliente e nao na cont
    # def eh_inadimplente(self, cliente):
    #     pass

    # aula 5
    # def get_saldo(self):
    #     return self.__saldo

    # aula 5
    # def get_titular(self):
    #     return self.__titular

    # aula 5
    # def get_limite(self):
    #     return self.__limite

    # Aula 6

    # aula 5
    # def set_limite(self, limite):
    #     self.__limite = limite

    #   Aula 6 - Utilizando get e set
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero


    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}