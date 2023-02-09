# treinando a função sorted e seus parâmetros
from operator import attrgetter
usuarios = [
    ("Andrea", 35, 1987),
    ("Neuza", 63, 1959),
    ("Eloisa", 9, 2013)
]

sorted(usuarios)                # ordem padrão ascendente
sorted(usuarios, reverse=True)  # ordem descendente

sorted(usuarios, key=lambda usuarios: usuarios[0])  # ordena pelo nome
sorted(usuarios, key=lambda usuarios: usuarios[1])  # ordena pela idade
sorted(usuarios, key=lambda usuarios: usuarios[2])  # ordena pelo ano

sorted(usuarios, key=lambda usuarios: usuarios[0], reverse=True)
sorted(usuarios, key=lambda usuarios: usuarios[1], reverse=True)
sorted(usuarios, key=lambda usuarios: usuarios[2], reverse=True)


# Boa práticas
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if (type(outro) != ContaSalario):
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>> codigo: {} Saldo: {}]".format(self._codigo, self._saldo)

# É possível obter o saldo da conta, importando o "attrgetter" e passar o valor do saldo por parâmetro.


for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)
