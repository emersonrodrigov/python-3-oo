from conta import Conta
from datas import Data
conta2 = Conta(321, "Marco", 100.0, 1000.0)

conta2.extrato()

conta2.deposita(100)
conta2.extrato()

conta2.saca(50)
conta2.extrato()



# Coletor de lixo
# Dentro da máquina virtual, na execução do Python, existe um processo que
# procura esses objetos esquecidos. Os itens inutilizados serão apagados e o
# espaço livre em memória será reutilizado
conta = Conta(123, "Nico", 55.5, 1000.0) # garbage de colector remove essa referencia
conta = Conta(123, "Nico", 55.5, 1000.0)

# None
#  conta e outraRef aponta para o mesmo endereço de memoria.
outraRef = conta

# Tira a referencia de uma variavel
outraRef = None; # equivale ao null do Java

data1 = Data(10,2,2018)

data1.formatada()