# funcao decoradora potencializa, modifica ou substitui a logica ou a funcionalidade de uma funcao ou metodo que recebeu a funcao decoradora


# vamos criar a funcao decoradora

def master(msg):
    def imprime():
        print("Essa eh a funcao Master\n")
        msg()
    return imprime


## como usar uma funcao decoradora ##
# utilizamos @ nome da funcao decoradora
## juntamente com a funcao que iremos chamar ##


# criar a ssegunda funcao para utilizar a funcao decoradora

def chamaFuncao():
    print("Esta chamando a funcao sec")


# chamaFuncao()


# decorando a funcao com o decorador

@master
def chamaFuncao():
    print(">>Esta chamando a funcao sec")

chamaFuncao()
