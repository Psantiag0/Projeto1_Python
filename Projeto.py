banco_de_dados = []

def criar_tarefa():
    tarefa = {}
    tarefa["Nome"] = input("Digite o nome da tarefa: ")
    tarefa["Descrição"] = input("Digite a descrição: ")
    tarefa["Categoria"] = input("Digite a categoria: ")
    tarefa["Prioridade"] = int(input("Digite a prioridade(1-3): "))
    tarefa["Status"] = False
    banco_de_dados.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefa():
    print(banco_de_dados)
listar_tarefa()

def prioridade_tarefa():
    nova_lista = sorted(banco_de_dados, key=lambda x: x["Prioridade"])
    print(nova_lista)
prioridade_tarefa()

def categoria_tarefa():
    nova_lista = sorted(banco_de_dados, key=lambda x: x["Categoria"])
    print(nova_lista)
categoria_tarefa()

# def concluir_tarefa():



while True:
    print("Bem vindo ao task v1.0!")
    print("1 - Criar tarefa")
    print("2 - Listar tarefa")
    print("3 - Ordenar tarefas por Prioridade")
    print("4 - Ordenar tarefas por Categoria")
    print("5 - Marcar tarefa como concluída")
    print("6 - Apagar tarefa")
    print("0 - Sair")
    op = int(input("Digite a opção: "))
    if op < 0 or op > 6:
        print("Opção inválida.")
    elif op == 1:
        criar_tarefa()
    elif op == 2:
        listar_tarefa()
    elif op == 3:
        prioridade_tarefa()
    elif op == 4:
        categoria_tarefa()
    # elif op == 5:
    #     concluir_tarefa()
    # elif op == 6:
    #     apagar_tarefa()
    elif op == 0:
        print("Fechando programa.")
        break
