# Salvar em json a lista do outro exercício

import shutil
import os
import json

def cria_arquivo():
    if not os.path.exists('Lista de Tarefas.json'):
        with open('Lista de Tarefas.json', 'w', encoding='utf-8') as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=2)

def adicionar_valor_ao_arquivo(tarefa):
    tarefas = []
    if os.path.exists('Lista de Tarefas.json'):
        with open('Lista de Tarefas.json', 'r', encoding='utf-8') as arquivo:
            try:
                tarefas = json.load(arquivo)
            except json.JSONDecodeError:
                tarefas = []
    tarefas.append(tarefa)
    with open('Lista de Tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

def lista_valores():
    if not os.path.exists('Lista de Tarefas.json'):
        return ""
    with open('Lista de Tarefas.json', 'r', encoding='utf-8') as arquivo:
        try:
            tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            tarefas = []
        return '\n'.join(tarefas)

def desfazer_alteracao(i):
    i = str(i)
    shutil.copyfile("Lista de Tarefas.json", "backup.json" + i)
    with open('Lista de Tarefas.json', 'r', encoding='utf-8') as arquivo:
        try:
            tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            tarefas = []
    tarefas = tarefas[:-1]
    with open('Lista de Tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

def refazer_alteração(i):
    shutil.copyfile("backup.json" + i, "Lista de Tarefas.json")

cria_arquivo()
i = 0
diretorio = os.getcwd()

while True:
    print("Comandos: Listar, Desfazer, Refazer, Sair")
    comando_tarefa = input("Digite um dos comandos acima ou a sua tarefa: ")
    comando_tarefa = comando_tarefa.lower()

    if comando_tarefa == 'sair':
        for arquivo in os.listdir(diretorio):
            if arquivo.startswith("backup.json"):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
        break

    elif comando_tarefa == 'listar':
        print("\nLista de Compras:\n")
        print(lista_valores())

    elif comando_tarefa == 'desfazer':
        if not os.path.exists('Lista de Tarefas.json'):
            print("Não temos o que desfazer")
            continue
        with open('Lista de Tarefas.json', 'r', encoding='utf-8') as arquivo:
            try:
                tarefas = json.load(arquivo)
            except json.JSONDecodeError:
                tarefas = []
        if not tarefas:
            print("Não temos o que desfazer")
            continue
        desfazer_alteracao(i)
        i += 1
        print("\nLista de Compras:\n")
        print(lista_valores())

    elif comando_tarefa == 'refazer':
        i -= 1
        if i < 0:
            print("Não tem o que refazer!")
            i += 1
            continue
        i_str = str(i)
        refazer_alteração(i_str)
        print("\nLista de Compras:\n")
        print(lista_valores())

    else:
        adicionar_valor_ao_arquivo(comando_tarefa)
        print("\nLista de Compras:\n")
        print(lista_valores())
