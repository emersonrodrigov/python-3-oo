
import conta

#  Dados da conta - Orientacao Objeto

numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0

print("Dados da conta 1 => Número: {} | Nome: {} | Saldo: {} | Limite: {} ".format(numero, titular, saldo,
                                           limite))

c1 = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.0}

print("Dados conta 2 {} ".format(c1))

print("Nova conta {}".format(conta.cria_conta(123, "Nico", 55.0, 1000.0)))

