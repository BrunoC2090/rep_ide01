# ler o arquivo que esta dentro da pasta arquivos


# criando a variavel de leitura do arquivo


import os

arq2 = os.path.basename(
    "C://Users//Bruno//Desktop//Bruno//rep_ide01//Aula 2//Manipulacao de Arquivos//arquivos//arquivo.txt")
# = open(os.path, 'arquivo.txt', 'r')

arq = open(arq2, 'r')
print(arq.read)

#arq1 = open('arquivos/arquivo.txt', 'r')
# print(arq1.read())
# arq1.close()
