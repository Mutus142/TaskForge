from database.connection import conectar_banco

def editar_task():

    task = input("Qual Tarefa voce quer editar? ")

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("select tiutlo from tarefa where titulo = %s", (task,))
            resultado = cursor.fetchone()

            if resultado is not None:
                
                print('''
                O que voce quer editar nessa tarefa?
                1 - Titulo
                2 - Prioridade
                ''')

                try:
                    escolha = int(input("Escolha uma opção: "))
                except ValueError:
                    print("Escolha um valor valido!")

                if escolha == 1:
                    editar_titulo()

                elif escolha == 2:
                    editar_prioridade()

                else:
                    print("Opção invalida!")