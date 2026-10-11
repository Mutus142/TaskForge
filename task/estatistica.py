
from database.connection import conectar_banco
import time


def estatisticas():

    print("Qual estatistica voce quer ver?")
    print('''
    1 - Tarefas Cadastradas
    2 - Tarefas Concluidas
    3 - Tarefas Pendentes
    4 - Estatisticas Gerais   
    5 - Voltar ao Menu principal 
''')

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Valor invalido, Testar outro!")

        if opcao == 1:
            task_cad()

        elif opcao == 2:
            task_con()

        elif opcao == 3:
            task_pen()

        elif opcao == 4:
            est_geral()

        elif opcao == 5:
            print("Voltando...")
            return