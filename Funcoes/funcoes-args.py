# funcoes args possui um numero ilimitado de argumentos
# possui uma variacao dinamica de argumento dentro de uma funcao
# onde o retorno da mesma sera em formato de tupla
# * args (retorna em tupla)
# ** kwargs (retorna in dict)
def soma(*args):
    print(args)


## chamar funcao soma valor ##


def soma_valor(*args):
    total = 0
    for value in args:
        total = value+total
    return total


print(soma_valor(5, 7, 2, 89, 12, 33))

print("\n#############################")
