import os
import psycopg
from database.connection import conectar_banco

class Tarefa:

    def __init__(self, id, titulo, prioridade, concluida):

        self.id = id
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluida = concluida


def ver_task():

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM tarefas ORDER BY id")
            registro = cursor.fetchall()

    print("\n========== TASKFORGE ==========")
    print("         SUAS TAREFAS")
    print("===============================")

    if not registro:
        print("\nNenhuma tarefa cadastrada.")
    else:
        for tarefa in registro:
            id, titulo, prioridade, concluida = tarefa

            situacao = "Concluída" if concluida else "Pendente"

            print(f"\nID:         {id}")
            print(f"Título:     {titulo}")
            print(f"Prioridade: {prioridade}")
            print(f"Situação:   {situacao}")
            print("-------------------------------")

    print("===============================\n")



def adicionar_task():

    prioridades = ["Alta", "Moderada", "Baixa"]

    print("""
========================================
          TASKFORGE v1.1
========================================
          ADICIONAR TAREFA
========================================
    """)

    titulo = input("Título da tarefa: ").strip()

    print("""
----------------------------------------
         PRIORIDADES DISPONÍVEIS
----------------------------------------
 [1] Alta
 [2] Moderada
 [3] Baixa
----------------------------------------
    """)

    prioridade = input("Digite a prioridade: ").strip().capitalize()

    if prioridade in prioridades:

        situacao = False

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tarefas (titulo, prioridade, concluida) VALUES (%s, %s, %s)",
                    (titulo, prioridade, situacao)
                )

        print(f"""
========================================
       TAREFA ADICIONADA!
========================================
 Título:     {titulo}
 Prioridade: {prioridade}
 Situação:   Pendente
========================================
        """)

    else:
        print("""
========================================
          PRIORIDADE INVÁLIDA!
========================================
 Utilize uma das opções disponíveis:

 - Alta
 - Moderada
 - Baixa
========================================
        """)


def remove_task():

    print("\n========== TASKFORGE ==========")
    print("         REMOVER TAREFA")
    print("===============================")

    titulo = input("\nTítulo da tarefa: ").strip()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT TITULO FROM TAREFAS WHERE TITULO = %s",
                (titulo,)
            )
            registro = cursor.fetchone()

            if registro is not None:
                cursor.execute(
                    "DELETE FROM TAREFAS WHERE TITULO = %s",
                    (titulo,)
                )

                print("\n-------------------------------")
                print("  Tarefa removida com sucesso!")
                print(f"  Título: {titulo}")
                print("===============================\n")

            else:
                print("\n-------------------------------")
                print("  Tarefa não encontrada!")
                print("===============================\n")



def concluir_task():

    print("\n========== TASKFORGE ==========")
    print("         CONCLUIR TAREFA")
    print("===============================")

    titulo = input('Qual é a tarefa que deseja concluir? ').strip()

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT TITULO FROM TAREFAS WHERE TITULO = %s",
                (titulo,)
            )

            registro = cursor.fetchone()

            if registro is not None:
                cursor.execute(
                    "UPDATE TAREFAS SET CONCLUIDA = TRUE WHERE TITULO = %s",
                    (titulo,)
                )

                print("\n-------------------------------")
                print("  Tarefa concluída com sucesso!")
                print(f"  Título: {titulo}")
                print("===============================\n")

            else:
                print("\n-------------------------------")
                print("  Tarefa não encontrada!")
                print("===============================\n")

            