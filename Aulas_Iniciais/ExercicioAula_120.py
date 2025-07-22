# Salvar em json a lista do outro exercício

import json
import copy

lista_tarefas = []
lista_tarefas_backup = []
i =0

def listar_tarefas():
    print('\nLISTA DE TAREFAS\n')
    for tarefa in lista_tarefas:
        print ('\t', tarefa)

def desfazer_ultimo():
    global lista_tarefas_backup, i

    if not lista_tarefas:
        print("Lista VAZIA")
        return

    lista_tarefas.pop()
    with open('Lista de Tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)

    listar_tarefas()
    i -= 1

def refazer_alteracao(index):
    global lista_tarefas_backup, i

    if i >= (len(lista_tarefas_backup)):
        print('Não tem o que refazer')
        return
    
    lista_tarefas.append(lista_tarefas_backup[i])
    with open('Lista de Tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
    
    listar_tarefas()
    
    i += 1

def adicionar_tarefa(comando):
    global lista_tarefas_backup, i

    lista_tarefas.append(comando)
    with open('Lista de Tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
    
    lista_tarefas_backup = copy.deepcopy(lista_tarefas)
    listar_tarefas()

    i += 1

while True:
    print('')
    print('Digite um dos comandos abaixo:')
    print('LISTAR, DESFAZER, REFAZER, SAIR')
    print('OU escreva o nome de uma tarefa para adicionar a lista:')
    comando = input('COMANDO: ')
    comando_lower = comando.lower()

    if comando_lower == 'listar':
        listar_tarefas()
    
    elif comando_lower == 'desfazer':
        desfazer_ultimo()
        
    elif comando_lower == 'refazer':
        refazer_alteracao(i)

    elif comando_lower == 'sair':
        print("sair")
        break
    
    else:
        adicionar_tarefa(comando_lower)