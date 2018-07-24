
from conta import Conta
from cliente import Cliente
conta = Conta(123, "Nico", 55.5, 1000.0)

print(f"{conta.saldo}")


print(f"{conta.titular}")


conta.limite = 1000.0
print(f"{conta.limite}")



#  Teste Cliente

c = Cliente("Nico");
c.nome = "Nico Alterado"
# c.nome = 'Nico Alterado'
print(c.nome)


#  Acessando Conta com as propriedades de get e set
conta = Conta(123, "Nico", 55.5, 1000.0)
conta.limite = 2000.0
print(conta.limite)

