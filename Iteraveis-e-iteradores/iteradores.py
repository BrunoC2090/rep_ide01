# todos objetos como listas, tuplas, dics, strings
# variaveis são considerados objetos iteraveis


# Exemplo

lista = ['Joao', 1, 'Pedro', 50]

# Como checar se objeto eh iteravel
# metodo mágico chamado '__iter__'
# duplos underline são chamados de dunder
# outra funcao chamada de hasattr (checa os atributos do objeto)

# checando se o objeto eh iteravel
print(hasattr(lista, '__iter__'))

cidade = "Floripa"
print(hasattr(cidade, '__iter__'))

print("\n\n")
# executar um iterador em um iteravel

# for s in cidade:
#   print(s)

# vamos entender o processo de um iterador
# for eh o principal iterador do python
# Sendo que ele transforma os objetos iteraveis em iteradores e percorre os seus itens de memoria
# Analisando o for e como funciona
# Transformando o iteravel em iterador
# Funcao iter transforma um iteravel em iterador

nome = "Bruno Costa"
iternome = iter(nome)
print(type(iternome))
# utilizar metodo magico '__next__' o next ele itera a memoria dos objetos
print(hasattr(iternome, '__next__'))
print(next(iternome))
print(next(iternome))
print(next(iternome))
print(next(iternome))
print(next(iternome))
print(next(iternome))
print("Separa a iteração ou laço\n")
for n in iternome:
    print(n)
print(next(iternome))
