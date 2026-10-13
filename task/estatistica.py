
from database.connection import conectar_banco
import time


def estatisticas(usuario_id):

    print("""
========================================
          TASKFORGE v1.5
========================================
        MENU DE ESTATÍSTICAS
========================================

 [1] Tarefas cadastradas
 [2] Tarefas concluídas
 [3] Tarefas pendentes
 [4] Estatísticas gerais
 [5] Tarefas atrasadas
 [6] Voltar ao menu principal

========================================
    """)

    try:
        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("""
========================================
           OPÇÃO INVÁLIDA!
========================================
 Digite um número de 1 a 6.
========================================
        """)
        return

    if opcao == 1:
        task_cad(usuario_id)

    elif opcao == 2:
        task_con(usuario_id)

    elif opcao == 3:
        task_pen(usuario_id)

    elif opcao == 4:
        est_geral(usuario_id)

    elif opcao == 5:
        task_atr(usuario_id)

    elif opcao == 6:
        print("\n[INFO] Voltando ao menu principal...")
        return

    else:
        print("""
========================================
           OPÇÃO INVÁLIDA!
========================================
 Escolha uma opção entre 1 e 6.
========================================
        """)


def task_cad(usuario_id):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM tarefas
                WHERE usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado = cursor.fetchone()

            if resultado[0] > 0:

                print(f"""
========================================
          TASKFORGE v1.5
========================================
         TAREFAS CADASTRADAS
========================================

 Total de tarefas: {resultado[0]}

 [OK] Consulta realizada com sucesso!

========================================
                """)

            else:

                print("""
========================================
          TASKFORGE v1.5
========================================
         TAREFAS CADASTRADAS
========================================

 Nenhuma tarefa cadastrada até agora!

========================================
                """)


def task_con(usuario_id):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(id)
                FROM tarefas
                WHERE concluida = TRUE
                AND usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado = cursor.fetchone()

            if resultado[0] > 0:

                print(f"""
========================================
          TASKFORGE v1.5
========================================
         TAREFAS CONCLUÍDAS
========================================

 Total de tarefas concluídas: {resultado[0]}

 [OK] Consulta realizada com sucesso!

========================================
                """)

            else:

                print("""
========================================
          TASKFORGE v1.5
========================================
         TAREFAS CONCLUÍDAS
========================================

 Nenhuma tarefa concluída até agora!

========================================
                """)


def task_pen(usuario_id):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(id)
                FROM tarefas
                WHERE concluida = FALSE
                AND usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado = cursor.fetchone()

            if resultado[0] > 0:

                print(f"""
========================================
          TASKFORGE v1.5
========================================
          TAREFAS PENDENTES
========================================

 Total de tarefas pendentes: {resultado[0]}

 [OK] Consulta realizada com sucesso!

========================================
                """)

            else:

                print("""
========================================
          TASKFORGE v1.5
========================================
          TAREFAS PENDENTES
========================================

 Nenhuma tarefa pendente no momento!

========================================
                """)


def est_geral(usuario_id):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM tarefas
                WHERE usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado1 = cursor.fetchone()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(id)
                FROM tarefas
                WHERE concluida = TRUE
                AND usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado2 = cursor.fetchone()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(id)
                FROM tarefas
                WHERE concluida = FALSE
                AND usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado3 = cursor.fetchone()

    print(f"""
========================================
          TASKFORGE v1.5
========================================
         ESTATÍSTICAS GERAIS
========================================

 Tarefas cadastradas: {resultado1[0]}
 Tarefas concluídas:  {resultado2[0]}
 Tarefas pendentes:   {resultado3[0]}

========================================
    """)


def task_atr(usuario_id):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM tarefas
                WHERE vencimento < CURRENT_DATE
                AND concluida = FALSE
                AND usuario_id = %s
                """,
                (usuario_id,)
            )

            resultado = cursor.fetchone()

            if resultado[0] > 0:

                print(f"""
========================================
          TASKFORGE v1.5
========================================
           TAREFAS ATRASADAS
========================================

 Total de tarefas atrasadas: {resultado[0]}

 [AVISO] Existem tarefas fora do prazo!

========================================
                """)

            else:

                print("""
========================================
          TASKFORGE v1.5
========================================
           TAREFAS ATRASADAS
========================================

 Total de tarefas atrasadas: 0

 [OK] Nenhuma tarefa atrasada!

========================================
                """)
