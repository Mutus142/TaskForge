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

    print(registro)
