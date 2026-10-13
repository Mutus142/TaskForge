
from user.cadastro import cad_user
from database.connection import conectar_banco
from menu import menu_inicial
import time


def tela_login():

    print("""
========================================
          TASKFORGE v1.5
========================================
           SISTEMA DE LOGIN
========================================

 Bem-vindo ao TaskForge!

 Faça seu login ou cadastre um usuário.

========================================
    """)

    return login()


def login():

    try:
        nome_user = input("\nDigite seu usuário: ").strip()

    except ValueError:
        print("\n[ERRO] Valor inválido!")
        return

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT id, username FROM usuarios WHERE username = %s",
                (nome_user,)
            )

            resultado = cursor.fetchone()

            if resultado is not None:

                usuario_id = resultado[0]

                print("""
========================================
           USUÁRIO LOCALIZADO!
========================================
 Informe sua senha para continuar.
========================================
                """)

                try:
                    senha_user = input("Digite sua senha: ")

                except ValueError:
                    print("\n[ERRO] Valor inválido!")
                    return

                with conectar_banco() as conexao:
                    with conexao.cursor() as cursor:
                        cursor.execute(
                            """
                            SELECT senha_hash
                            FROM usuarios
                            WHERE username = %s AND senha_hash = %s
                            """,
                            (nome_user, senha_user)
                        )

                        resultado_senha = cursor.fetchone()

                        if resultado_senha is None:

                            print("""
========================================
             SENHA INVÁLIDA!
========================================
 A senha informada está incorreta.
========================================
                            """)

                            time.sleep(2)

                            print("""
========================================
          O QUE DESEJA FAZER?
========================================
 [1] Tentar novamente
 [2] Cadastrar usuário
========================================
                            """)

                            try:
                                escolha = int(input("Escolha uma opção: "))

                            except ValueError:
                                print("\n[ERRO] Opção inválida!")
                                return

                            if escolha == 1:
                                return login()

                            elif escolha == 2:
                                cad_user()
                                return login()

                            else:
                                print("\n[ERRO] Opção inválida!")
                                return

                        else:

                            print(f"""
========================================
          LOGIN REALIZADO!
========================================

 Bem-vindo ao TaskForge!

 Usuário: {nome_user}
 ID:      {usuario_id}

 [OK] Autenticação realizada!

========================================
                            """)

                            time.sleep(1)
                            return menu_inicial(usuario_id)

            else:

                print("""
========================================
        USUÁRIO NÃO ENCONTRADO!
========================================

 O usuário informado não está cadastrado.

 [1] Tentar novamente
 [2] Cadastrar novo usuário
 [0] Sair

========================================
                """)

                escolha = input("Escolha uma opção: ").strip()

                if escolha == "1":
                    return login()

                elif escolha == "2":
                    cad_user()
                    return login()

                elif escolha == "0":
                    print("\n[INFO] Encerrando TaskForge...")
                    return

                else:
                    print("\n[ERRO] Opção inválida!")
                    return login()
