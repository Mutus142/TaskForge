
from task.task_service import ver_task
from task.task_service import adicionar_task
from task.task_service import remove_task
from task.task_service import concluir_task
from task.editar import editar_task
from task.estatistica import estatisticas


def menu_inicial(usuario_id):

    while True:

        print("""
========================================
              TASKFORGE
               v1.5
========================================
 [1] Ver tarefas
 [2] Adicionar tarefa
 [3] Remover tarefa
 [4] Editar tarefa
 [5] Concluir tarefa
 [6] Estatísticas
 [0] Sair
----------------------------------------
        """)

        try:
            opcao = int(input(" >> Escolha uma opção: "))

        except ValueError:
            print("\n [!] Opção inválida. Digite um número.")
            continue

        if opcao == 1:
            ver_task(usuario_id)

        elif opcao == 2:
            adicionar_task(usuario_id)

        elif opcao == 3:
            remove_task(usuario_id)

        elif opcao == 4:
            editar_task(usuario_id)

        elif opcao == 5:
            concluir_task(usuario_id)

        elif opcao == 6:
            estatisticas(usuario_id)

        elif opcao == 0:
            print("\n [>] Encerrando TaskForge...")
            break

        else:
            print("\n [!] Opção inválida!")
