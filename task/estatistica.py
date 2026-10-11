
from database.connection import conectar_banco
import time


def estatisticas():

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
 [5] Voltar ao menu principal

========================================
    """)

    try:
        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("""
========================================
           OPÇÃO INVÁLIDA!
========================================
 Digite um número de 1 a 5.
========================================
        """)
        return

    if opcao == 1:
        task_cad()

    elif opcao == 2:
        task_con()

    elif opcao == 3:
        task_pen()

    elif opcao == 4:
        est_geral()

    elif opcao == 5:
        print("\n[INFO] Voltando ao menu principal...")
        return

    else:
        print("""
========================================
           OPÇÃO INVÁLIDA!
========================================
 Escolha uma opção entre 1 e 5.
========================================
        """)


def task_cad():

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM tarefas"
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


def task_con():

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(id) FROM tarefas WHERE concluida = TRUE"
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


def task_pen():

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(id) FROM tarefas WHERE concluida = FALSE"
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


def est_geral():

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM tarefas"
            )

            resultado1 = cursor.fetchone()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(id) FROM tarefas WHERE concluida = TRUE"
            )

            resultado2 = cursor.fetchone()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(id) FROM tarefas WHERE concluida = FALSE"
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
