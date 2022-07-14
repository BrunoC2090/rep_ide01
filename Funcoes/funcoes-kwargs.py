## funcoes kwargs ##
## tambem trabalham com N argumentos na funcao ##
## porem retorno eh em dicionario ##

def saudacao(**kwargs):
    print(kwargs)

## chamar funcao ##


saudacao(manha='bom dia', tarde='boa tarde', noite='boa noite')


def saudacao_dia(**kwargs):
    for hora, saudacao in kwargs.items():
        print(f'Durante a {hora} dizemos {saudacao}')


saudacao_dia(manha='bom dia', tarde='boa tarde')
