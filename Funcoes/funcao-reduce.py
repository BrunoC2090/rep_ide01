# reduzir um valor  a um unico valor baseado na funcao aplicada

from functools import reduce

reduce

lista = [2, 7, 10, 3, 78]


def mult(x, y):
    return x+y


print(reduce(mult, lista))

lista2 = [45, 1, 100, 4, 12]


def testamaior(x, y): return x if (x > y) else y


print(reduce(testamaior, lista2))
