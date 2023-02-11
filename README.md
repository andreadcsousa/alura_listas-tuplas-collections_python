# Python Collections parte 1: listas e tuplas

Abordagem de lista, tupla, existência das arrays como tipos dentro do Python e das arrays do numpy.

1. [Listas e operações](#1-listas-e-operações)
2. [Tuplas](#2-tuplas)
3. [Polimorfismo e arrays](#3-polimorfismo-e-arrays)
4. [Igualdade](#4-igualdade)
5. [Outros builtins](#5-outros-builtins)
6. [Ordem natural](#6-ordem-natural)
7. [Ordenação customizada](#7-ordenação-customizada)
8. [Ordenação total](#8-ordenação-total)

Saiba mais sobre o curso [aqui](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas) ou acompanhe minhas anotações abaixo. ⬇️

## 1. Listas e operações

### **Introdução as coleções e lista**

Para entender melhor os elementos de listas, utiliza-se métodos de inserção e remoção de itens, numa lista de objetos. A função `.append()` adiciona um item ao final da lista, mesmo que o item já exista na lista. Já a função `.remove()` apaga a primeira inserção de um item da lista, por exemplo:

```py
idades = [39, 30, 27]

idades.append(18)       # retorna [39, 30, 27, 18]

type(idades)            # retorna list
len(idades)             # retorna 4

idades[0]               # retorna 39

idades.append(15)       # retorna [39, 30, 27, 18, 15]

for idade in idades:
    print(idade)        # retorna 39 30 27 18 15

idades.remove(30)       # retorna [39, 27, 18, 15]

idades.append(27)       # retorna [39, 27, 18, 15, 27]
idades.remove(27)       # retorna [39, 18, 15, 27]

idades.clear()          # remove todos os itens da lista
```

### **Mais operações em lista e list comprehension**

Para realizar uma verificação no itens da lista, pode-se perguntar isso utilizando o `in` ou pode-se utilizar o `if` para verificar e já fazer uma modificação na lista. Para inserir um item em um ponto específico da lista, utiliza-se a função `insert(posição, valor)`, diferente do append que só recebe um argumento, por exemplo:

```py
idades = [39, 18, 15, 27]

28 in idades            # retorna False
15 in idades            # retorna True

if 15 in idades:        # retorna [39, 18, 27]
    idades.remove(15)

if 28 in idades:        # retorna [39, 18, 27], pois 28 não existe na lista
    idades.remove(28)

idades.append(19)       # retorna [39, 18, 27, 19]
idades.insert(0, 20)    # retorna [20, 39, 18, 27, 19]

idades = [20, 39, 18]

idades.append(27, 19)   # retorna erro
idades.append([27, 19]) # retorna [20, 39, 18, [27, 19]]

for elemento in idades:
    print("Recebi o elemento", elemento)

# Recebi o elemento 20
# Recebi o elemento 39
# Recebi o elemento 18
# Recebi o elemento [27, 19]
```

Para resolver a questão da inserção de itens na lista, sem que eles retornem outra lista dentro da anterior, usa-se a função `.extend()`. No caso de querer criar uma lista a partir de outra, cria-se uma lista vazia, depois utiliza-se a função `.append()` para adicionar mais itens, por exemplo:

```py
idades.extend([27, 19])       # retorna [20, 39, 18, 27, 19]

idades = [20, 39, 18, 27, 19]
idades_no_ano_que_vem = []

for idade in idades:          # retorna [21, 40, 19, 28, 20] na lista "idades_no_ano_que_vem"
    idades_no_ano_que_vem.append(idade + 1)
idades_no_ano_que_vem

# utilizando list comprehension = função + iteração + condição
idades = [20, 39, 18, 27, 19]
idades_no_ano_que_vem = []

[(idade + 1) for idade in idades]           # retorna [21, 40, 19, 28, 20]
[(idade) for idade in idades if idade > 21] # retorna [39, 27] pois filtra números menores que 21

# definindo uma função com list comprehension, aplicando filtros e transformações
def proximo_ano(idade):
    return idade + 1

[proximo_ano(idade) for idade in idades if idade > 21]
```

### **Problemas da mutabilidade da lista**

> Python tem objetos mutáveis e imutáveis. Os mutáveis contêm estado interno, como atributos, que podem ser alterados durante sua existência. Já os imutáveis não podem ser alterados e seu estado pode ser definido somente em sua inicialização.

São mutáveis:

- `list` estrutura de dados que armazena dados em sequência, com índice
- `dict` coleção de itens desordenados, com identificador
- `set` coleção de itens desordenados, não duplicados

São imutáveis:

- `tuple` estrutura de dados que armazena dados em sequência, com índice
- `str` cadeia de caracteres que representam textos
- `int` conjunto de números inteiros (positivos, negativos, zero)
- `float` conjunto de números decimais (possuem partes fracionadas)

```py
def processa_visualizacao(lista):
    print(len(lista))

idades = [16, 21, 29, 56, 43]
processa_visualizacao(idades)   # retorna 5 como tamanho da lista e [16, 21, 29, 56, 43] como valores


def processa_visualizacao(lista):
    print(len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]
processa_visualizacao(idades)   # retorna 5 como tamanho da lista e [16, 21, 29, 56, 43, 13] como valores


# trabalhando com a mutabilidade das listas
def processa_visualizacao(lista = []):      # lista vazia
    print(len(lista))
    lista.append(13)
processa_visualizacao()     # retorna 0
processa_visualizacao()     # retorna 1
processa_visualizacao()     # retorna 2
processa_visualizacao()     # retorna 3

def processa_visualizacao(lista = []):
    print(len(lista))
    print(lista)            # imprimindo a lista
    lista.append(13)
processa_visualizacao()     # retorna 0 []
processa_visualizacao()     # retorna 1 [13]
processa_visualizacao()     # retorna 2 [13, 13]
processa_visualizacao()     # retorna 3 [13, 13, 13]

def processa_visualizacao(lista = list()):  # lista de objetos vazia
    print(len(lista))
    print(lista)
    lista.append(13)
processa_visualizacao()     # retorna 0 []
processa_visualizacao()     # retorna 1 [13]
processa_visualizacao()     # retorna 2 [13, 13]
processa_visualizacao()     # retorna 3 [13, 13, 13]

def processa_visualizacao(lista = None):    # nada, falta de valor
    if lista == None:
        lista = list()      # se a lista não tem nada, cria uma nova lista
    print(len(lista))
    print(lista)
    lista.append(13)
processa_visualizacao()     # retorna 0 []
processa_visualizacao()     # retorna 0 []
processa_visualizacao()     # retorna 0 []
processa_visualizacao()     # retorna 0 []
```

## 2. Tuplas

### **Listas com objetos de classes nossas**

Ao criar listas com objetos que são instanciados por classes, é necessário atentar para a referência que for criada para cada objeto da lista. Um objeto pode ser referenciado várias vezes, mesmo que seja instanciado apenas uma vez na classe. Como exemplo, têm-se 2 contas distintas, mas uma delas é referenciada em duplicidade, veja:

```py
# criação da classe "ContaCorrente"
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Código {} Saldo {} <<]".format(self.codigo, self.saldo)

# criação das contas
conta_andrea = ContaCorrente(15)
conta_andrea.deposita(500)
print(conta_andrea)                 # retorna [>> Código 15 Saldo 500 <<]

conta_eloisa = ContaCorrente(18)
conta_eloisa.deposita(1000)
print(conta_eloisa)                 # retorna [>> Código 18 Saldo 1000 <<]

# análise dos objetos criados
contas = [conta_andrea, conta_eloisa]
for conta in contas:
    print(conta)                 # retorna [>> Código 15 Saldo 500 <<] e [>> Código 18 Saldo 1000 <<]

# referência das contas
contas = [conta_andrea, conta_eloisa, conta_andrea]
#           posição 0     posição 1     posição 2
print(contas[0])
print(contas[2])            # todos retornam [>> Código 15 Saldo 500 <<]
print(contas[conta_andrea]) # pois é a mesma conta, o mesmo objeto referenciado várias vezes
```

### **Tuplas, objetos e anemia**

Ao definir que a posição da lista seja o número da agência, todas as contas passam a ter o código da agência como sua posição da lista. Não sendo mais possível chamar as contas pela posição em que aparecem na lista e, sim, pela sua referência base, ou seja, o nome da conta.

```py
def deposito_em_conta(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_andrea, conta_eloisa]
print(contas[0], contas[1])

deposito_em_conta(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])  # imprime o código da agência e os dados das contas

deposito_em_conta(contas)
print(contas[0], contas[1], contas[2])  # retorna erro, pois o 76 não faz referência a uma conta
```

Quando não se quer que uma lista seja mutável, o correto é usar a `tupla`. Representada entre parênteses, pode conter um ou mais valores e não aceita inserção de dados após a criação da lista. Contudo, pode-se criar uma função com uma `variação funciona`l, separando o comportamento dos dados.

```py
andrea = ('Andrea', 35, 1987)
neuza = ('Neuza', 63, 1959)

andrea.append(978264)   # retorna erro


conta_andrea = (15, 100)
conta_andrea[1]

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

deposita(conta_andrea)                  # retorna 15, 200 / nova tupla
conta_andrea                            # retorna 15, 100 / variável original

conta_andrea = deposita(conta_andrea)   # retorna 15, 200 / reatribuição da variável original
conta_andrea
```

> Listas nos levam a variação orientada a objetos e tuplas nos levam a variação funcional.

- Se a posição indica alguma coisa, provavelmente tem um tamanho fixo, então provavelmente é uma tupla.
- Se a posição não tem tipo definido, específico, sendo tudo do mesmo tipo, então provavelmente é uma lista.

### **Tupla de objetos e lista de tuplas**

É possível criar listas de tuplas. Tais listas irão armazenar informações que foram passadas anteriormente em tuplas com dados individuais dos "usuários". A tupla não deixa adicionar ou remover elementos dela, mas é possível adicionar e remover "referências de referenciados", ou seja, alterar os objetos da tupla.

```py
usuarios = [andrea, neuza]
usuarios
# retorna [('Andrea', 35, 1987) e ('Neuza', 63, 1959)]

usuarios.append(('Eloisa', 9, 2013))
usuarios
# retorna [('Andrea', 35, 1987) ('Neuza', 63, 1959) e ('Eloisa', 9, 2013)]

usuarios[0]                     # retorna o usuário na posição 0 - [('Andrea', 35, 1987)]
usuarios[0][0] = 'Andrea Sousa' # retorna erro, pois não é possível modificar os valores de uma tupla

# identificando contas e depósitos
conta_andrea = ContaCorrente(15)
conta_andrea.deposita(500)

conta_eloisa = ContaCorrente(18)
conta_eloisa.deposita(1000)

contas = (conta_andrea, conta_eloisa)

for conta in contas:
    print(conta)        # retorna [>> Código 15 Saldo 500 <<] e [>> Código 18 Saldo 1000 <<]

contas[0].deposita(300) # o depósito foi possível, porque a tupla não foi alterada, apenas seu objeto

for conta in contas:
    print(conta)        # retorna [>> Código 15 Saldo 800 <<] e [>> Código 18 Saldo 1000 <<]
```

## 3. Polimorfismo e arrays

### **Listas e polimorfismo**

Para criar variáveis com atributos privados deve-se adicionar um underline `_` antes do atributo. Sabendo disso, é possível trabalhar o conceito de herança, na qua uma classe pode herdar atributos e métodos de outra classe, evitando repetição do código.

> Polimorfismo, em Python, é a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua superclasse, e o programa saber qual método deve ser invocado, especificamente (da super ou sub). Ou seja, o objeto tem a capacidade de assumir diferentes formas (polimorfismo).

```py
# criando uma classe para definir os atributos que as contas irão possuir
class Conta:
    def __init__(self, codigo):
        # anteriormente não foi utilizado o "_" para tornar o atributo privado
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>> Código {} Saldo {} <<]".format(self._codigo, self._saldo)

# utilizando os conceitos de herança e polimorfismo nas subclasses com atributos da classe "Conta"
class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2
    
class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

# verificando os dados das contas individualmente
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)              # retorna [>> Código 16 Saldo 998 <<]

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)              # retorna [>> Código 17 Saldo 1007.0 <<]


# verificando dados de várias contas em simultâneo
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)            # retorna [>> Código 16 Saldo 998 <<] e [>> Código 17 Saldo 1007.0 <<]
```

### **Arrays e Numpy**

Array é um módulo utilizado para trabalhar com mais eficácia com números. Isso quer dizer que o `array` pode armazenar mais de um item ao mesmo tempo. Funciona como uma coleção ordenada de elementos e cada valor representa valores básicos, tais: caracteres `str`, inteiros `int`, números de ponto flutuante `float`. É como uma lista, porém mais restrito, pois é especificado um `type code` na criação do objeto:

- `'b'` tipo int                        - `'B'` tipo int
- `'h'` tipo int                        - `'H'` tipo int
- `'i'` tipo int                        - `'I'` tipo int
- `'l'` tipo int                        - `'L'` tipo int
- `'q'` tipo int                        - `'Q'` tipo int
- `'f'` tipo float                      - `'u'` tipo caractere unicode
- `'d'` tipo double

> Para o dia-a-dia usual do Python utiliza-se as listas. Em situações específicas em que se tem um conjunto bem pequeno de elementos, onde cada posição indica uma coisa é comum usar as tuplas. E onde costuma ser importante um alto desempenho de funções matemáticas com Python é muito comum utilizar uma biblioteca, chamada Numpy.

Evita-se utilizar array puro do Python, para trabalhos numéricos, costuma-se utilizar o Numpy. Para instalar o Numpy pelo terminal, digita-se `pip install nummpy` e para importar no arquivo Python, digita-se `import numpy as np`. Após instalar e importar, pode-se declarar variáveis e valores, realizar cálculos e trabalhar com vários tipo de dados científicos.

```py
# importando array
import array as arr

arr.array('d', [1, 3.5])        # necessário indicar o tipo de dado

# importando numpy
import numpy as np

np.array([1, 3.5])

# declarando uma variável
numeros = np.array([1, 3.5])
numeros                         # retorna "array([1. , 3.5])"
numeros + 3                     # retorna "array([4. , 6.5])"
```

> `Duck typing` é um conceito relacionado à tipagem dinâmica, onde o tipo ou a classe de um objeto é menos importante do que os métodos que ele define. Quando você usa duck tiping, não verifica os tipos. Em vez disso, você verifica a presença de um determinado método ou atributo.

## 4. Igualdade

### **Objetos de class**

Os objetos das classes em Python aceitam dois tipos de operações:

- Referências a atributos
- Instanciação

> Referências a atributos de classe utilizam a sintaxe padrão utilizada para quaisquer referências a atributos em Python: `obj.nome`. Nomes de atributos válidos são todos os nomes presentes dentro do espaço de nomes da classe, quando o objeto classe foi criado.

Dado o código abaixo, têm-se que `MyClass.i` e `MyClass.f` são referências a atributos válidas, que retornam valores, respectivamente, inteiro e objeto da função. Para instanciar a classe, basta chamar ela, sem parâmetros. Isso devolve uma nova instância da classe [linha 417] e atribui o objeto resultante à variável `x`.

***Instanciar é o mesmo que chamar ou invocar uma função ou classe.***

```py
class MyClass:
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
```

### **Métodos especiais de classes**

Métodos de classes são predefinições utilizadas em orientação a objeto para definir parâmetros aos objetos que possam inicializar, comparar... Ou para que subclasses possam herdar estados dessa classe base.

- `__init__` criada na construção do objeto, inicializa a classe base e as subclasses dela
  > Nenhum valor diferente de None pode ser retornado por "__init__()"
- `__str__` calcula a representação da string para exibição de um objeto de valor string
- `__eq__` usado quando se quer comparar um objeto com outro, funciona como o `is` ou o `==`
- `__len__` se refere a contagem de elementos discretos e retorna um número inteiro

```py
# inicialização
def __init__(self, codigo):
    self._codigo = codigo

# string
def __str__(self):
    return "[>> Código {} <<]".format(self._codigo)

# igualdade
def __eq__(self, outro):
    return self._codigo == outro._codigo

# tamanho
def __len__(self):
    return len(self.codigo)
```

## 5. Outros builtins

### **Built-ins**

Para imprimir a posição dos elementos da lista, juntamente aos seus valores correpondentes, pode-se utilizar a `range(len())` para acessar cada item da sequência com a ajuda do seu índice. Ou `enumerate()` para retornar um contador com uma chave para cada valor em um objeto, facilitando o acesso aos itens da coleção.

```py
idades = [15, 87, 65, 56, 32, 49, 37]

for idade in idades:
    print(idade)                # retorna os itens da lista

range(len(idades))              # retorna a quantidade de itens da lista "range(0, 8)"

# correto
for i in range(len(idades)):
    print(i, idades[i])         # retorna a posição dos itens e seus valores

list(enumerate(idades))         # retorna uma lista de tuplas contendo posição e valor

for valor in enumerate(idades):
    print(valor)                # retorna tuplas contendo posição e valor em cadeia

# correto
for indice, idade in enumerate(idades):
    print(indice, idade)        # retorna posição e valor desempacotados (fora da lista e da tupla)
```

> Nas soluções acima, len() é usado para encontrar o comprimento da lista fornecida.
> Aplicar range(len(li)) cria uma sequência de números de 0 até len().
> Desse modo pode acessar cada item da lista usando seu índice com a ajuda de um loop for.

O valor retornado por `len()` é um inteiro que representa a quantidade de elementos do interável. No caso de strings, retorna cada letra de uma palavra. No caso de números, retorna cada valor que foi separado por vírgula.

## 6. Ordem natural

### **Ordenação básica**

A função `sorted()` serve para odernar itens de uma lista de forma ascendente, retornando uma nova lista ordenada baseada na lista original. Enquanto o método `list.sort()` modifica a lista em si e funciona bem caso a lista original não seja necessária.

```py
a = [5, 2, 3, 1, 4]

sorted(a)                   # retorna [1, 2, 3, 4, 5]

a.sort()
a                           # retorna [1, 2, 3, 4, 5]
```

## 7. Ordenação customizada

### **Ordenação de objetos sem ordem natural**

A função `sorted()` entrega o resultado de forma mais simples que o método `list.sort()`. Contudo, ao sortear uma lista em que os valores estão no formato string, a ordem natural do sorted é que o alfabeto em maiúsculo vem antes do alfabeto em minúsculo, ou seja, vai ordenar uma lista de nomes, priorizando essa diferença.

```py
nomes = ["Neuza", "andrea", "Eloisa"]

sorted(nomes)       # retorna ['Eloisa', 'Neuza', 'andrea']

nomes.sort()
nomes               # retorna ['andrea', 'Eloisa', 'Neuza']
```

A função sorted aceita ainda 2 atributos. A `key` recebe um parâmetro-chave para a ordenação da lista, através de uma função ou atributo da função. O `reverse` que vem, por padrão, "False", mas quando definido para "True", retorna a lista em ordem descendente.

> As strings são classificadas alfabeticamente e os números são classificados numericamente.

```py
# reverse
a = [5, 2, 3, 1, 4]

sorted(a, reverse=True)     # retorna [5, 4, 3, 2, 1]

a.sort(reverse=True)
a                           # retorna [5, 4, 3, 2, 1]

# key
usuarios = [("Andrea", 35, 1987), ("Neuza", 63, 1959), ("Eloisa", 9, 2013)]

sorted(usuarios, key=usuario[0])                # ordena pelo nome ascendente
sorted(usuarios, key=usuario[1], reverse=true)  # ordena pela idade descendente
```

### **Implementando o __lt__**

O método `__lt__` significa "menor que" (less than, em inglês) e serve para comparar valores. Existem outros métodos semelhantes que comparam os valores de outra forma, de acordo com a necessidade do usuário. No entanto, esses métodos podem retornar qualquer valor, que pode ou não ser interpretado como um valor booleano.

> Por convenção, "False" e "True" são retornados para uma comparação bem-sucedida.

- `__lt__(a, b)` é o equivalente a `a < b` "menor que"
- `__gt__(a, b)` é o equivalente a `a > b` "maior que"
- `__le__(a, b)` é o equivalente a `a <= b` "menor igual"
- `__ge__(a, b)` é o equivalente a `a >= b` "maior igual"
- `__eq__(a, b)` é o equivalente a `a == b` "igual"
- `__en__(a, b)` é o equivalente a `a != b` "diferente"

```py
...
def __lt__(self, outro):
    return self._saldo < outro._saldo
...

# definição das contas
conta_andrea = ContaSalario(16)
conta_andrea.deposita(500)

conta_eloisa = ContaSalario(17)
conta_eloisa.deposita(1000)

# comparação das contas
conta_andrea < conta_eloisa     # retorna "True"
conta_andrea > conta_eloisa     # retorna "False"
```

## 8. Ordenação total

### **Ordenação completa e functools**

Ao utilizar o `__lt__` torna-se dispensável adicionar o `__gt__`. Isso porque são comparações idênticas. Para uma ordenação completa, em que se quer utilizar o "menor igual", por exemplo, pode-se utilizar o `@total_ordering`.

> Dada uma classe que define um ou mais métodos de ordenação de comparação avançados, esse decorador de classe fornece o resto. Isso simplifica o esforço envolvido na especificação de todas as operações de comparação ricas possíveis. A classe deve definir um dos __lt__(), __le__(), __gt__() ou __ge__(). Além disso, a classe deve fornecer um método __eq__().

Com isso, ao utilizar `__eq__` e `__lt__` numa classe, os demais métodos de comparação não funcionam, pois um representa a igualdade e o outro retorna se é menor ou maior. O menor igual e o maior igual seriam a junção destes ou os substituiriam. Porém, com o total_ordering isso não é necessário.

```py
...
# compara se o tipo de conta é igual a outra conta e se os valores de código e saldo são iguais também
def __eq__(self, outro):
    if type(outro) != ContaSalario:
        return False
    return self._codigo == outro._codigo and self._saldo == outro._saldo

# compara se o saldo é menor ou maior ao outro saldo, ordenando pelo código se os saldos forem diferentes
def __lt__(self, outro):
    if self._saldo != outro._saldo:
        return self._saldo < outro._saldo
    return self._codigo < outro._codigo
...

# importa o total_ordering e dá para uma classe várias outras comparações, ao definir "__eq__" e "__lt__".
from functools import total_ordering
@total_ordering
class...
```

⬆️ [Voltar ao topo](#python-collections-parte-1-listas-e-tuplas) ⬆️