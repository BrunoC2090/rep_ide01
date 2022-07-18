# sao chamados de elementos de sintaxe especifica
# sao utilizados para manipulas listas de forma otimizada
# utilizando poucas linhas de codigo

# uma das principais formas de uso de codigo de metodo procedural em python PEP 202


listaNumeros = [1, 4, 5, 7, 10]

lc1 = [multiplica * 2 for multiplica in listaNumeros]

print(lc1)

listaPares = [pares for pares in range(20)if pares % 2 == 0]
print(listaPares)

listaNomes = ["Joao", "Jose", "Jefferson"]
lc2 = [troca.replace("J", "j") for troca in listaNomes]
print(lc2)

