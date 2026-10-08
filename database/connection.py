import os
import psycopg

def conectar_banco():

    return psycopg.connect(
        host= "localhost",
        port= 5432,
        dbname= "TaskForge",
        user= "taskforge_user",
        password=os.environ["TASKFORGE_DB_PASSWORD"]
    )