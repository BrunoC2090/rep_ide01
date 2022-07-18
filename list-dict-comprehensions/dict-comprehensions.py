# sao chamados de elementos de sintaxe especifica
# sao utilizados para manipulas dicts de forma otimizada
# utilizando poucas linhas de codigo

# uma das principais formas de uso de codigo de metodo procedural em python PEP 202


listaDict = [
    ('valor', 10),
    ('valor2', 8),
    ('valor3', 30)
]

d1 = {c: v for c, v in listaDict}
print(d1)
