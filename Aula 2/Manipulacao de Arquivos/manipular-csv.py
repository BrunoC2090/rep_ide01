# para manipular arquivos csv, utilizamos a lib CSV

import csv
from typing import KeysView

with open('arquivos/nomes.csv', 'w+', newline="")as fcsv:
    escrever = csv.writer(fcsv, delimiter=',')
    escrever.writerow(("Nome", "Sobrenome", "Idade"))
    escrever.writerow(("Joao", "Ricardo", 37))
    escrever.writerow(("Juca", "Souza", 43))
    escrever.writerow(("Alberto", "Cunha", 67))

## Ler Arquivo Criado ##

with open('arquivos/nomes.csv', 'r') as fcsv2:
    ler = csv.reader(fcsv2)
    # print(list(ler))
    lista1 = list(ler)
    print(lista1)

    for itera in lista1:
        print(itera)

## transformar a saida do csv em dicionario ##

with open('arquivos/nomes.csv', 'r') as fcsv3:
    ler_dict = csv.DictReader(fcsv3)

    ## iterar valores ##

    # for dic in ler_dict:
    #   print(dic.get('Nome'), dic.get('Idade'))

    ## iterar valores das chaves ##
    # for dic in ler_dict:
    #   print(dic['Nome'])  # ["Nome"])


with open('arquivos/arquivo1.csv', 'r') as arq1:
    ler = csv.reader(arq1)
    # for i in ler:
    #   print(i)
    ##vai printar a lista##
    lista2 = list(ler)
    print(lista2)
