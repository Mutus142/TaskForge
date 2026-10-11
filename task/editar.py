
from database.connection import conectar_banco
import time


def editar_task():

    task = input("\nDigite o título da tarefa que deseja editar: ").strip()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute(
                "SELECT titulo FROM tarefas WHERE titulo = %s",
                (task,)
            )

            resultado = cursor.fetchone()

            if resultado is not None:

                print("""
========================================
           EDITAR TAREFA
========================================
 [1] Editar título
 [2] Editar prioridade
========================================
                """)

                try:
                    escolha = int(input("Escolha uma opção: "))

                except ValueError:
                    print("\n[ERRO] Digite uma opção numérica válida!")
                    return

                if escolha == 1:
                    editar_titulo(task)

                elif escolha == 2:
                    editar_prioridade()

                else:
                    print("\n[ERRO] Opção inválida!")

            else:
                print("\n[ERRO] Tarefa não encontrada!")


def editar_titulo(task):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM tarefas WHERE titulo = %s",
                (task,)
            )

            resultado = cursor.fetchone()

            if resultado is None:
                print("\n[ERRO] Tarefa não encontrada!")
                return

            titulo_novo = input("\nDigite o novo título da tarefa: ").strip()

            if not titulo_novo:
                print("\n[ERRO] O título não pode estar vazio!")
                return

            if titulo_novo == task:
                print("\n[AVISO] O novo título é igual ao atual!")
                return

            else:
                with conectar_banco() as conexao:
                    with conexao.cursor() as cursor:

                        cursor.execute(
                            "UPDATE tarefas SET titulo = %s WHERE titulo = %s",
                            (titulo_novo, task)
                        )

                print(f"""
========================================
        TAREFA ATUALIZADA!
========================================
 Título anterior: {task}
 Novo título:     {titulo_novo}
========================================
                """)

                time.sleep(5)

                print("""
========================================
         O QUE DESEJA FAZER?
========================================
 [1] Editar outra tarefa
 [2] Voltar ao menu principal
========================================
                """)

                try:
                    escolha = int(input("Escolha uma opção: "))

                except ValueError:
                    print("\n[ERRO] Digite uma opção numérica válida!")
                    return

                if escolha == 1:
                    editar_task()

                elif escolha == 2:
                    print("\n[INFO] Voltando ao menu principal...")
                    return

                else:
                    print("\n[ERRO] Opção inválida!")
