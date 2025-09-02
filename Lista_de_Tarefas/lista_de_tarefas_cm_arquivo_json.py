# Criando um Arquivo.json para salvar as Listas de Tarefas

import json # Obrigatório para usar funções "JSON"

Tarefas = []

def salvar_tarefas():
    with open('tarefas.json', 'w') as arquivo: # 'W' cria um arquivo novo ou sobre-escreve um já existente
        json.dump(Tarefas, arquivo) # 'dump' é a função que salva os dados em um arquivo 'Json'
    print("Tarefas salvas com sucesso!")

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo: # 'R' lê um arquivo Json já existente
            Tarefas = json.load(arquivo) # 'load' é a função que carrega o arquivo 'Json', sendo o oposto de 'dump'
            print("Tarefas carregadas com sucesso!")
            return Tarefas
    except:
        print("Nenhum arquivo de Tarefas encontrado!\n Começando uma nova lista.")
        return [] # Retorna uma lista vazia caso não aja um arquivo Json salvo.

def adicionar_tarefa(nome, prioridade): 
    Tarefa = {'nome': nome, 'prioridade' : prioridade} 
    Tarefas.append(Tarefa)
    print("\nTarefa adicionada: ", Tarefa)

def remover_tarefa(nome): 
    for Tarefa in Tarefas:
            if Tarefa['nome'] == nome:
                Tarefas.remove(Tarefa)
                print("Tarefa removida")
                break
            else:
                print("Essa tarefa não esta na lista.")

def listar_tarefas(): 
    print("\nLista de Tarefas:")
    for Tarefa in Tarefas: 
        print(f"- {Tarefa['nome']} (Prioridade: {Tarefa['prioridade']})") 

Tarefas = carregar_tarefas()

while True:

    print("\n**Menu de opções**\n")
    print("1- Adicionar Tarefa.")
    print("2- Remover Tarefa.")
    print("3- Lista de Tarefa.")
    print("4- Salvar Tarefas.")
    print("5- Sair.")

    opcao = input("Escolha uma opção: ")

    if opcao == '1': 
        nome = input("\nDigite o nome da tarefa: ")
        prioridade = input("\nDigite a prioridade da Tarefa: ") 
        adicionar_tarefa(nome, prioridade)
    
    elif opcao == '2':
        nome = input("\nDigite o nome da tarefa a ser removida: ")
        remover_tarefa(nome)

    elif opcao == '3':
        listar_tarefas()

    elif opcao == '4':
        salvar_tarefas()

    elif opcao == '5': 
        print("\nSaindo...")
        break 

    else:
        print("\nOpção inválida.")

'''
Sempre verificar quando definir funções, se elas possuem '()', pois se faltar isso, 
pode dar um Bug na execução do código, e o erro não é mostrado no painel, ele aponta para outro
lugar, como foi o caso na linha '41'
'''