# para maninupular arquivos json temos que utilizar a lib json

import json


cadastro_pessoa = {

    "1": {
        "Nome": "Joao",
        "Idade": 35,
        "Sexo": "Masculino",
        "Data Nascimento": "29/12/1985"
    },
    "2": {
        "Nome": "Juca",
        "Idade": 34,
        "Sexo": "Masculino",
        "Data Nascimento": "12/12/1985"
    },
    "3": {
        "Nome": "Leandro",
        "Idade": 50,
        "Sexo": "Masculino",
        "Data Nascimento": "01/01/1970"
    },
    "4": {
        "Nome": "Rita",
        "Idade": 23,
        "Sexo": "Feminino",
        "Data Nascimento": "12/09/1997"
    }
}

# iterar esse dicionario

for chave, valor in cadastro_pessoa.items():
    print(chave, valor)

# para transformar dicionarios em arquivos formato json utilizamos a funcao json.dumps

dadosDic = json.dumps(cadastro_pessoa, indent=4)
print(dadosDic)

# salvar json em arquivo

with open('arquivos/cadastro_pessoa2.json', 'w+')as j:
    json.dump(cadastro_pessoa, j, indent=4)

# lendo json funcao json.load
with open('arquivos/cadastro_pessoa2.json', 'r')as f:
    le_json = json.load(f)
    print(le_json)
    for v in le_json.values():
        print(v)
