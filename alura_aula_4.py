from conta import Conta

 # Atributos Privados

conta = Conta(321, "Marco", 100.0, 1000.0)

# e possivel acessar o atributo privado
# porem não faça isso
print(conta._Conta__limite)


conta = Conta(123, "Nico", 55.5, 1000.0)

conta2 = Conta(321, "Marco", 100.0, 1000.0)
#
# valor = 10.00
#
# conta2.saca(valor)
# conta.deposita(valor)

#  encapsulamento
conta2.transfere(10.0, conta)


#
# S - Single responsibility principle
# O - Open/closed principle
# L - Liskov substitution principle
# I - Interface segregation principle
# D - Dependency inversion principle