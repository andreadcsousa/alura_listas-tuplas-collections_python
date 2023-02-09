# Utilizando o método "__init__" para definir a área de um retângulo
class Area:
    def area(self):
        return self.altura * self.largura


a = Area()
a.altura = 25
a.largura = 75
a.area()

# O código acima retorna o valor 1875 para área do retângulo.
# Porém, como não utiliza o método "__init__", não deixa claro as propriedades do elemento.


class Area:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura


b = Area(123, 90)
b.area()

# O caso acima, torna melhor a leitura do código e seu uso durante a construção do objeto.
# A própria construção da classe já define os parâmetros do objeto em questão.
