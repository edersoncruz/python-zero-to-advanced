from pprint import pprint
import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

#Deep Copy
novos_produtos = copy.deepcopy(produtos)

#Aumentar em 10%
novos_produtos = [{**prod,'preco':  round(prod['preco'] *1.1, 2)} for prod in produtos]

#Deep Copy
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

#Ordenar nome decrescente
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)

#Deep Copy
produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_nome)

#Ordenar por preço crescente
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])

print('LISTA ORIGINAL')
pprint(produtos)

print('LISTA COM 10% A MAIS')
pprint(novos_produtos)

print('ORDENDADOS POR NOME DECRESCENTE')
pprint(produtos_ordenados_por_nome)

print('ORDENDADOS POR PRECO CRESCENTE')
pprint(produtos_ordenados_por_preco)
