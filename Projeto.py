banco_de_dados = []

print("Bem vindo ao Newtask v1.0!\n")

def criar_tarefa():
    tarefa = {}
    tarefa["Nome"] = input("Digite o nome da tarefa: ")
    tarefa["Descrição"] = input("Digite a descrição: ")
    tarefa["Categoria"] = input("Digite a categoria: ")
    tarefa["Prioridade"] = int(input("Digite a prioridade(1-3): "))
    if tarefa["Prioridade"] < 1 or tarefa["Prioridade"] > 3:
        print("Digite um número de 1 a 3. Tente novamente.")
        return
    tarefa["Status"] = False
    banco_de_dados.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")


def listar_tarefa():
    print("Listando tarefas por ordem de entrada:\n")
    for i, tarefa in enumerate(banco_de_dados):
        print(f"Tarefa {i + 1}: {tarefa['Nome']}, Categoria: {tarefa['Categoria']}, Prioridade: {tarefa['Prioridade']}, Concluída: {tarefa['Status']}")


def prioridade_tarefa():
    nova_lista = sorted(banco_de_dados, key=lambda x: x["Prioridade"])
    print("Tarefas Ordenadas por prioridade:\n")
    for i, tarefa in enumerate(nova_lista):
        status = "Concluída" if tarefa["Status"] else "Pendente"
        if nova_lista != []:
            print(f"Tarefa {i + 1}. Nome: {tarefa['Nome']}, Descrição: {tarefa['Descrição']}, Categoria: {tarefa['Categoria']}, Prioridade: {tarefa['Prioridade']}, Status: {status}")


def categoria_tarefa():
    nova_lista = sorted(banco_de_dados, key=lambda x: x["Categoria"])
    print("Tarefas Ordenadas por Categoria:\n")
    for i, tarefa in enumerate(nova_lista):
        status = "Concluída" if tarefa["Status"] else "Pendente"
        if nova_lista != []:
            print(f"Tarefa {i + 1}. Nome: {tarefa['Nome']}, Descrição: {tarefa['Descrição']}, Categoria: {tarefa['Categoria']}, Prioridade: {tarefa['Prioridade']}, Status: {status}")


def concluir_tarefa():
    listar_tarefa()
    indice = int(input("\nDigite o número da tarefa que você deseja concluir: "))
    if 0 < indice <= len(banco_de_dados):
        banco_de_dados[indice - 1]["Status"] = True
        print(f"Tarefa {indice} concluída com sucesso!")
    else:
        print("Tarefa inexistente. Tente novamente")
        return
    

def apagar_tarefa():
    listar_tarefa()
    indice = int(input("\nDigite o número da tarefa que você deseja apagar: "))
    if 0 < indice <= len(banco_de_dados):
        del banco_de_dados[indice - 1]
        print(f"Tarefa {indice} removida com sucesso!")
    else:
        print("Tarefa inexistente. Tente novamente.")    
        return


while True:
    print("\nEscolha uma das opções:\n")
    print("1 - Criar tarefa")
    print("2 - Listar tarefa")
    print("3 - Ordenar tarefas por Prioridade")
    print("4 - Ordenar tarefas por Categoria")
    print("5 - Marcar tarefa como Concluída")
    print("6 - Apagar tarefa")
    print("0 - Sair\n")
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
    elif op == 5:
        concluir_tarefa()
    elif op == 6:
        apagar_tarefa()
    elif op == 0:
        print("Fechando programa.")
        break
