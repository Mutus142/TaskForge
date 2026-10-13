
from datetime import datetime, date
from database.connection import conectar_banco


class Tarefa:

    def __init__(self, id, titulo, prioridade, concluida, vencimento, usuario_id):

        self.id = id
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluida = concluida
        self.vencimento = vencimento
        self.usuario_id = usuario_id


def ver_task(usuario_id):

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, titulo, prioridade, concluida, vencimento
                FROM tarefas
                WHERE usuario_id = %s
                ORDER BY id
                """,
                (usuario_id,)
            )
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

            if vencimento is not None:
                data_formatada = vencimento.strftime("%d/%m/%Y")
            else:
                data_formatada = "Sem prazo"

            print(f"""
----------------------------------------
 ID:         {id}
 Título:     {titulo}
 Prioridade: {prioridade}
 Vencimento: {data_formatada}
 Situação:   {situacao}
----------------------------------------
            """)

    print("========================================\n")


def adicionar_task(usuario_id):

    prioridades = ["Alta", "Moderada", "Baixa"]

    print("""
========================================
          TASKFORGE v1.5
========================================
           ADICIONAR TAREFA
========================================
    """)

    titulo = input("Título da tarefa: ").strip()

    if not titulo:
        print("\n[ERRO] O título não pode estar vazio!")
        return

    print("""
----------------------------------------
        PRIORIDADES DISPONÍVEIS
----------------------------------------
 - Alta
 - Moderada
 - Baixa
----------------------------------------
    """)

    prioridade = input("Digite a prioridade: ").strip().capitalize()

    if prioridade in prioridades:

        situacao = False

        data = input("\nData de vencimento (DD/MM/AAAA): ")

        try:
            data_convertida = datetime.strptime(
                data, "%d/%m/%Y"
            ).date()

        except ValueError:
            print("""
========================================
             DATA INVÁLIDA!
========================================
 Utilize o formato DD/MM/AAAA.
========================================
            """)
            return

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
                    """
                    INSERT INTO tarefas
                    (titulo, prioridade, concluida, vencimento, usuario_id)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (titulo, prioridade, situacao, data_convertida, usuario_id)
                )

        print(f"""
========================================
           TAREFA ADICIONADA!
========================================
 Título:     {titulo}
 Prioridade: {prioridade}
 Vencimento: {data_convertida.strftime('%d/%m/%Y')}
 Situação:   Pendente

 [OK] Tarefa vinculada à sua conta!
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


def remove_task(usuario_id):

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
                """
                DELETE FROM tarefas
                WHERE titulo = %s AND usuario_id = %s
                RETURNING id
                """,
                (titulo, usuario_id)
            )

            registros = cursor.fetchall()

            if registros:

                print(f"""
========================================
          TAREFA REMOVIDA!
========================================
 Título: {titulo}
 Registros removidos: {len(registros)}

 [OK] Tarefa removida com sucesso!
========================================
                """)

            else:

                print("""
========================================
         TAREFA NÃO ENCONTRADA!
========================================
 Nenhuma tarefa com esse título
 foi encontrada na sua conta.
========================================
                """)


def concluir_task(usuario_id):

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
                """
                UPDATE tarefas
                SET concluida = TRUE
                WHERE titulo = %s AND usuario_id = %s
                RETURNING id
                """,
                (titulo, usuario_id)
            )

            registros = cursor.fetchall()

            if registros:

                print(f"""
========================================
           TAREFA CONCLUÍDA!
========================================
 Título:   {titulo}
 Situação: Concluída
 Registros atualizados: {len(registros)}

 [OK] Tarefa finalizada com sucesso!
========================================
                """)

            else:

                print("""
========================================
         TAREFA NÃO ENCONTRADA!
========================================
 Nenhuma tarefa com esse título
 foi encontrada na sua conta.
========================================
                """)
