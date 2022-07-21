# os geradores que pode ser funcoes ou estruturas do tipo comprehensions
# os geradores otimizam o uso de memoria de um codigo
# os geradores liberam a memoria no mesmo momento de execucao
# onde os objetos normais ou iteradores aguardam concluir todo o processo em memoria para depois descarregar


# funcao normal

import time
from numpy import append
import sys


def funcNormal():
    l = []
    for n in range(100):
        l.append(n)
        time.sleep(0.1)
    return l


# print(funcNormal())

# Declarar a funcao geradora utilizando a funcao yeld q torna a fguncao geradora


def funcGerador():
    for n in range(100):
        yield n
        time.sleep(0.1)
# converter os for's em variavel e chamar como gerador


gen = funcGerador()
# for i in gen:
#    print(i)
# funcao geradora nao tem return
# remove for's de dentro do codigo e traz pra funcao otimizando a execucao no local onde for estava chama-se a funcao geradora


lc1 = [l for l in range(100)]
# print(lc1)

lc2 = (l for l in range(100))
# for l in lc2:
#   print(l)
print(type(lc1))
print("\n")
print(type(lc2))

# testar o valor de memoria de um elemento no codigo
# vamos usar o getsizeof
# precisa importar sys

print(sys.getsizeof(lc1))
print(sys.getsizeof(lc2))
print("batata")
