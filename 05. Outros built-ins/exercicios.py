# Numerando
idades = [15, 87, 37, 45, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

# Outra forma de obter uma lista enumerada pelas suas posições é utilizando a função "enumerate", pois ela enumera os valores automaticamente.

for indice, idade in enumerate(idades):
    print(indice, idade)
