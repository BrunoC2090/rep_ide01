## Funcoes com e sem argumento ##


## funcoes sem argumento ##


def oi():
    print("Ola pessoal")


oi()

## funcao com argumento ##


def soma(a, b):
    return a+b


s = soma(3, 5)
print(s)
print("\n")
print(soma(4, 2))

## Argumento padrao ##


def mult(a, b=3):
    return a*b


# sobrepondo arg
print(mult(4, 5))
# arg default
print(mult(2))


## Argumentos Args e Kwargs ##
# Args argumento generico quando nao sei qts parametros serao utilizados
