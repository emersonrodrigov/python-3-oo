class Cliente:

    def __init__(self, nome):
        # Para usar @Property devemos deixar as propriedas provadas
        self.__nome = nome

    # Get e Set de nome
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title() # title() -> Primeira letra da strinf maiúsculo

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome