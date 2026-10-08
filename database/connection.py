import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="TaskForge",
        user="taskforge_user",
        password=os.environ["TASKFORGE_DB_PASSWORD"]
    )