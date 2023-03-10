# -*- coding: utf-8 -*-
"""Objetos Próprios

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PN06fcdBLFkngO-Go1CKk-tylpGFiPSj
"""


class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Código {} Saldo {} <<]".format(self.codigo, self.saldo)


conta_andrea = ContaCorrente(15)
print(conta_andrea)

conta_andrea.deposita(500)
print(conta_andrea)

conta_eloisa = ContaCorrente(47685)
conta_eloisa.deposita(1000)
print(conta_eloisa)

contas = [conta_andrea, conta_eloisa]
print(contas)

contas = [conta_andrea, conta_eloisa]
for conta in contas:
    print(conta)

contas = [conta_andrea, conta_eloisa, conta_andrea]

print(contas[0])

conta_andrea.deposita(100)

print(contas[0])

print(conta_andrea)


def deposito_em_conta(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_andrea, conta_eloisa]
print(contas[0], contas[1])

deposito_em_conta(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

deposito_em_conta(contas)
print(contas[0], contas[1], contas[2])

andrea = ('Andrea', 35, 1987)
neuza = ('Neuza', 63, 1959)

# eloisa = (9, 'Eloisa', 2013) # ruim

andrea.append(978264)

conta_andrea = (15, 100)
# conta_andrea.deposita() # variação orientação a objeto
conta_andrea[1]

conta_andrea[1] += 100


def deposita(conta):  # variação funcional / separa o comportamento dos dados
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)


deposita(conta_andrea)

conta_andrea

conta_andrea = deposita(conta_andrea)
conta_andrea

usuarios = [andrea, neuza]
usuarios

usuarios.append(('Eloisa', 9, 2013))
usuarios

usuarios[0]

usuarios[0][0] = 'Andrea Sousa'

conta_andrea = ContaCorrente(15)
conta_andrea.deposita(500)

conta_eloisa = ContaCorrente(47685)
conta_eloisa.deposita(1000)

contas = (conta_andrea, conta_eloisa)

contas

for conta in contas:
    print(conta)

contas.append(56465)

contas[0].deposita(300)

for conta in contas:
    print(conta)
