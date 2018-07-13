
import conta_service

#  Dados da conta - Orientacao Objeto

numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0

print("Dados da conta 1 => Número: {} | Nome: {} | Saldo: {} | Limite: {} ".format(numero, titular, saldo,
                                           limite))

c1 = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.0}

print("Dados conta 2 {} ".format(c1))

print("Nova conta {}".format(conta_service.cria_conta(123, "Nico", 55.0, 1000.0)))


#  testando funcoes conta

conta = conta_service.cria_conta(123, "Nico", 55.0, 1000.0)
conta_service.deposita(conta, 15.0)
conta_service.extrato(conta)
conta_service.saque(conta, 20.0)
conta_service.extrato(conta)
