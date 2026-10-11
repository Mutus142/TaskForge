
import os
import psycopg
from datetime import datetime, date
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

    print("""
========================================
          TASKFORGE v1.5
========================================
             SUAS TAREFAS
========================================
    """)

    if not registro:
        print("""
----------------------------------------
       NENHUMA TAREFA CADASTRADA
----------------------------------------
    """)

    else:
        for tarefa in registro:
            id, titulo, prioridade, concluida, vencimento = tarefa

            situacao = "Concluída" if concluida else "Pendente"

            print(f"""
----------------------------------------
 ID:         {id}
 Título:     {titulo}
 Prioridade: {prioridade}
 Vencimento: {vencimento}
 Situação:   {situacao}
----------------------------------------
            """)

    print("========================================\n")


def adicionar_task():

    prioridades = ["Alta", "Moderada", "Baixa"]

    print("""
========================================
          TASKFORGE v1.5
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

        data = input("\nData de vencimento (DD/MM/AAAA): ")

        data_convertida = datetime.strptime(data, "%d/%m/%Y").date()

        if data_convertida < date.today():

            print(f"""
========================================
             DATA JÁ VENCIDA!
========================================
 Data informada: {data_convertida.strftime('%d/%m/%Y')}

 [AVISO] Esta data já passou!
========================================
            """)

        elif data_convertida == date.today():

            print(f"""
========================================
              VENCE HOJE!
========================================
 Vencimento: {data_convertida.strftime('%d/%m/%Y')}

 [AVISO] O prazo da tarefa é hoje!
========================================
            """)

        else:

            print(f"""
========================================
          VENCIMENTO DEFINIDO!
========================================
 Vencimento: {data_convertida.strftime('%d/%m/%Y')}

 [OK] A tarefa está dentro do prazo!
========================================
            """)

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tarefas (titulo, prioridade, concluida, vencimento) VALUES (%s, %s, %s, %s)",
                    (titulo, prioridade, situacao, data_convertida)
                )

        print(f"""
========================================
           TAREFA ADICIONADA!
========================================
 Título:     {titulo}
 Prioridade: {prioridade}
 Vencimento: {data_convertida}
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

    print("""
========================================
          TASKFORGE v1.5
========================================
            REMOVER TAREFA
========================================
    """)

    titulo = input("Título da tarefa: ").strip()

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

                print(f"""
========================================
          TAREFA REMOVIDA!
========================================
 Título: {titulo}

 [OK] Tarefa removida com sucesso!
========================================
                """)

            else:

                print("""
========================================
         TAREFA NÃO ENCONTRADA!
========================================
 Não foi possível localizar a tarefa.
========================================
                """)


def concluir_task():

    print("""
========================================
          TASKFORGE v1.5
========================================
           CONCLUIR TAREFA
========================================
    """)

    titulo = input("Qual tarefa deseja concluir? ").strip()

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

                print(f"""
========================================
           TAREFA CONCLUÍDA!
========================================
 Título:   {titulo}
 Situação: Concluída

 [OK] Tarefa finalizada com sucesso!
========================================
                """)

            else:

                print("""
========================================
         TAREFA NÃO ENCONTRADA!
========================================
 Não foi possível localizar a tarefa.
========================================
                """)
