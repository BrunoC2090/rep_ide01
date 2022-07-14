# funcao map -- aplicar uma funcao predefinida em cima de uma estrutura de dados

from cmath import sqrt
import math


lista = [1, 4, 6, 8, 10]


def soma(x):
    return x+2


print(list(map(soma, lista)))
# raiz quadrada dos elementos da lista

print(list(map(math.sqrt, lista)))
