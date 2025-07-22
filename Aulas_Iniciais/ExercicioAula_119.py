# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import shutil
import os

def cria_arquivo():
    with open('Lista de Tarefas.txt', 'w', encoding='utf-8') as arquivo:
        return ...

def adicionar_valor_ao_arquivo(tarefa):
    with open('Lista de Tarefas.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(tarefa + '\n')
    return ...

def lista_valores():
    with open('Lista de Tarefas.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        return conteudo

def desfazer_alteracao(i):
    i = str(i)
    shutil.copyfile("Lista de Tarefas.txt", "backup.txt" + i)
    
    with open('Lista de Tarefas.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        linhas = linhas [:-1]
   
    with open('Lista de Tarefas.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    

def refazer_alteração(i):
    shutil.copyfile("backup.txt" + i, "Lista de Tarefas.txt")

cria_arquivo()
i = 0
diretorio = os.getcwd()

while True:
    print("Comandos: Listar, Desfazer, Refazer, Sair")
    comando_tarefa = input("Digite um dos comandos acima ou a sua tarefa: ")
    comando_tarefa = comando_tarefa.lower()

    if comando_tarefa == 'sair':
        for arquivo in os.listdir(diretorio):
            if arquivo.startswith("backup"): 
                caminho_arquivo = os.path.join(diretorio, arquivo)
                if os.path.isfile(caminho_arquivo):  
                    os.remove(caminho_arquivo) 
        break

    elif comando_tarefa == 'listar':
        print("\nLista de Compras:\n" )
        print(lista_valores())

    elif comando_tarefa == 'desfazer':
        
        with open ('Lista de Tarefas.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        
        if linhas == []:
            print("Não temos o que desfazer")
            continue
        
        desfazer_alteracao(i)
        i += 1
        
        print("\nLista de Compras:\n" )
        print(lista_valores())
    
    elif comando_tarefa == 'refazer':
        i -= 1
        if i < 0:
            print("Não tem o que refazer!")
            i += 1
            continue
        
        i = str(i)
        refazer_alteração(i)
        i = int(i)
        
        print("\nLista de Compras:\n" )
        print(lista_valores())
        

    else:     
        adicionar_valor_ao_arquivo(comando_tarefa)
        print("\nLista de Compras:\n" )
        print(lista_valores())
    