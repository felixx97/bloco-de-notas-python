tarefas = []


def exibir_menu():

    while True:
        print("\n--- Menu: ---")
        print("1. Adicionar tarefa")
        print("2. Excluir tarefa")
        print("3. Atualizar status da tarefa")
        print("4. Registrar conclusão de tarefa")
        print("5. Listar tarefas")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            incluir_tarefa()
        elif escolha == '2':
            excluir_tarefa()
        elif escolha == '3':
            atualizar_status_tarefa()
        elif escolha == '4':
            registrar_conclusao()
        elif escolha == '5':
            listar_tarefas()
        elif escolha == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def incluir_tarefa():
    titulo = input("Digite o título da tarefa: ")
    data_hora = input("Digite a data e hora da tarefa (DD/MM/AAAA HH:MM): ")

    tarefa = {
        'titulo': titulo,
        'data_hora': data_hora,
        'status': 'em espera',
        "data_conclusao": ""
    }

    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas):
        print(
            f"{i + 1}. {tarefa['titulo']} - Status: {tarefa['status']} (criada em {tarefa['data_hora']})")
        if tarefa['data_conclusao']:
            print(f"   Concluída em: {tarefa['data_conclusao']}")


def excluir_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a ser excluída: ")) - 1
        if 0 <= indice < len(tarefas):
            del tarefas[indice]
            print("Tarefa excluída com sucesso!")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


def atualizar_status_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a ser atualizada: ")) - 1
        if 0 <= indice < len(tarefas):
            print("Escolha o novo status:")
            print("1 - Em espera")
            print("2 - Em andamento")
            print("3 - Concluída")
            opcao = input("Digite o número da opção: ")
            if opcao == '1':
                tarefas[indice]['status'] = 'em espera'
            elif opcao == '2':
                tarefas[indice]['status'] = 'em andamento'
            elif opcao == '3':
                tarefas[indice]['status'] = 'concluída'
                tarefas[indice]['data_conclusao'] = input(
                    "Digite a data de conclusão (DD/MM/AAAA HH:MM): ")
            else:
                print("Opção inválida.")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


def registrar_conclusao():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            if tarefas[indice]["status"] != "Feito":
                print("A tarefa ainda não está marcada como 'Feito'.")
                return
            data = input(
                "Digite a data e hora de conclusão (ex: 26/05/2025 16:00): ")
            tarefas[indice]["data_conclusao"] = data
            print("Data de conclusão registrada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")


exibir_menu()
