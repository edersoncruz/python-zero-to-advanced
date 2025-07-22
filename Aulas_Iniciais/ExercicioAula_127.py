# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

p1 = Pessoa('JOÃO', 29)
dic_p1 = vars(p1)
print(dic_p1)

with open('p1.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dic_p1, arquivo, ensure_ascii=False, indent=2) 
print ("Dados da instancia salvo no JSON")

with open('p1.json', 'r', encoding='utf-8') as arquivo:
    dados_p1 = json.load(arquivo)

p2 = Pessoa(dados_p1['nome'], dados_p1['idade'])
print(vars(p2))

with open('p2.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_p1, arquivo, ensure_ascii=False, indent=2) 
print ("Dados da instancia salvo no JSON 2")