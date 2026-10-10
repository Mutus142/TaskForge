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
            cursor.execute("select * from tarefas")
            registro = cursor.fetchall()

    print("\n========== TASKFORGE ==========")
    print("         SUAS TAREFAS")
    print("===============================")
    print(registro)
    print("===============================\n")

def adicionar_task():

    print("\n========== TASKFORGE ==========")
    print("       ADICIONAR TAREFA")
    print("===============================")

    titulo = input('Qual é o titulo? ')
    prioridade = input('Qual é a prioridade? ')
    situacao = False

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO tarefas (titulo, prioridade, concluida) VALUES (%s, %s, %s)", (titulo, prioridade, situacao))
            registro = cursor.fetchall()

    print("\n===============================")
    print("  Tarefa adicionada com sucesso!")
    print("===============================\n")


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

            