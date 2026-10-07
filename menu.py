while True:

    print("""
========================================
              TASKFORGE
               v0.1
========================================
 [1] Ver tarefas
 [2] Adicionar tarefa
 [3] Remover tarefa
 [4] Concluir tarefa
 [0] Sair
----------------------------------------
""")

    try:
        opcao = int(input(" >> Escolha uma opção: "))

    except ValueError:
        print("\n [!] Opção inválida. Digite um número.")

        if opcao == 1:
            ver_task()

        elif opcao == 2:
            add_task()

        elif opcao == 3:
            remove_task()

        elif opcao == 4:
            concluir_task()

        elif opcao == 0:
            print('Saindo...')
            break

        else:
            print('Opção invalida!')