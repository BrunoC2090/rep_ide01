# ler o arquivo que esta dentro da pasta arquivos


# criando a variavel de leitura do arquivo


import os

# arq2 = os.path.basename(
#  "C://Users//Bruno//Desktop//Bruno//rep_ide01//Aula 2//Manipulacao de Arquivos//arquivos//arquivo.txt")
# = open(os.path, 'arquivo.txt', 'r')

#arq = open(arq2, 'r')
# print(arq.read)

arq1 = open('arquivos/arquivo.txt', 'r')
print(arq1.read())
arq1.close()


# w+ opçao de gravar e ler + em conjunto com w quer dizer leitura
#arq2 = open('arquivos/arquivo.txt', 'w+')
#arq2.write("tem nova linha\n")
#arq2.write("pulo linha")
#arq2.seek(0, 0)
# print(arq2.read()) ## le o conteudo do arquivo
# arq2.close()

#arq3 = open('arquivos/arquivo.txt', 'a+')
#arq3.write("\ngravou a terceira linha")
#arq3.seek(0, 0)
# print(arq3.read())
# arq3.close()

## gerenciador de contexto de arquivos ##

with open('arquivos/arquivos1.txt', 'w+') as f:
    f.write("teste linha\n")
    f.write("teste linha2\n")
    f.write("Teste Acentuação")
    f.seek(0, 0)
    grava = str(f.read())
    print(grava)
## metodo a appenda novos dados ##

with open('arquivos/arquivos2.xls', 'w+') as f2:
    f2.write(grava)
    f2.seek(0, 0)
    print(f2.read())
