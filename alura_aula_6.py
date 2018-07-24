from conta import Conta


conta = Conta(123, "Nico", 55.5, 1000.0)

conta.saldo
conta.saca(1200.0 )

# conta.pode_sacar(100.0) # esse metodo tem que ser privado não podendo acessar por referencia
print(conta.saldo)

# Testando codigo banco
conta = Conta(123, "Nico", 55.5, 1000.0)

codigo_banco = Conta.codigo_banco()
print('codigo {}'.format(codigo_banco)) # Static Metodo
print(Conta.codigos_bancos()) # Static Metodo