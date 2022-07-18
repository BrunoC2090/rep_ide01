# retorna os elementos em tuplas
# e trunca(corta) os dados sempre na menor estrutura de dados
# comparada


listaInteiros = [1, 2, 3, 4, 5, 6, 7]
listaInteiros2 = [1, 1, 1, 1, 1]


dictVerduras = {1: 'teste', 2: "batata", 3: "Repolho", 4: 'Beterraba'}
dictFrutas = {1: 'Maça', 7: 'laranja', 3: "pera"}

junta = list(zip(dictVerduras, dictFrutas))
print(junta)
juntavalores = list(zip(dictFrutas.values(), dictVerduras.values()))
print(juntavalores)

# iterar resultado dos itens

for p in juntavalores:
    print(p)
