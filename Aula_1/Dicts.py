## dicionarios -- colecao desordenada em forma de chave  e valor ##
## nao possui indice ##
## utilizado em formato json ##
## pode ser mutavel, homogenea e heterogena ##

# o dicionario eh composto por:

exdic = {'chave': 'valor'}
estados_siglas = {'SC': 'Santa Catarina', 'pr': 'Parana',
                  'RS': 'Rio Grande do Sul', 'SP': 'Sao Paulo'}

print(estados_siglas.keys())

# testa se o valor de chave esta presente no dicionarion
# pode criar uma msg caso nao existir(else)
print(estados_siglas['RS'])
print(estados_siglas.get('SC', 'Nao tem'))

## Iterar dicionario ##
for value in estados_siglas:
    print(value, estados_siglas[value])
    if value == "RS":
        break
