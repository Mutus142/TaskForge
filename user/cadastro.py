from database.connection import conectar_banco


def cad_user():

    print("""
========================================
          TASKFORGE v1.5
========================================
        CADASTRO DE USUÁRIO
========================================
    """)

    nome_user = input("Qual é seu nome completo? ").strip()
    user = input("Qual é o nome de usuário? ").strip()
    senha = input("Digite sua senha: ")

    if not nome_user or not user or not senha:
        print("""
========================================
           DADOS INVÁLIDOS!
========================================
 Todos os campos são obrigatórios.
========================================
        """)
        return

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO usuarios (nome, username, senha_hash)
                VALUES (%s, %s, %s)
                """,
                (nome_user, user, senha)
            )

    print(f"""
========================================
        USUÁRIO CADASTRADO!
========================================

 Nome:    {nome_user}
 Usuário: {user}

 [OK] Cadastro realizado com sucesso!

========================================
    """)

    return