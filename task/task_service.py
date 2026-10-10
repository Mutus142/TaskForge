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

def adicionar_task():

    print('Adicione uma Tarefa! Prencha todas as especificaçĩes:')
    titulo = input('Qual é o titulo?')
    prioridade = input('Qual é a prioridade?')
    situacao = False

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO tarefas (titulo, prioridade, concluida) VALUES (%s, %s, %s)", (titulo, prioridade, situacao))
            registro = cursor.fetchall()

    print("Tarefa adicionada com sucesso!")
