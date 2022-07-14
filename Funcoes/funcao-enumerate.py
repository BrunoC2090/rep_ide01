## funcao enumerate -- enumera os indices de memoria de uma estrutura de dados ##

# lista

animais = ['cachorro', 'gato', 'onça', 'elefante']
print("saida enumeracao\n")
indexado = (list(enumerate(animais)))
print(list(indexado)[-1])
# for enumerate
for i, valor in enumerate(animais):
    print(i, valor)

# enumerando com condicao

for i, valor in enumerate(animais):
    if i >= 1:
        break
    else:
        print(valor)
