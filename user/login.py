
from database.connection import conectar_banco
import time

def tela_login():
    print('''
    Bem vindo ao TaskForge 1.5

    Faça seu login abaixo ou cadastre seu usuario!

    ''')

    def login():

        try:
            nome_user = input("Digite o seu usuario: ")
        except ValueError:
            print("Valor invalido!")
            return

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select username from usuarios where username = %s", (nome_user,)
                )
                resultado = cursor.fetchone()

                if resultado is not None:
                    print("Usuário validado!")

                    try:
                        senha_user = input("Digite a sua senha: ")
                    except ValueError:
                        print("Valor invalido!")
                        return

                    with conectar_banco() as conexao:
                        with conexao.cursor() as cursor:
                            cursor.execute(
                                "select senha_hash from usuarios where senha_hash = %s and username = %s", (senha_user, nome_user)
                            )
                            resultado_senha = cursor.fetchone()

                            if resultado_senha is not None:
                                print("Senha invalida!")
                                time.sleep(2)

                                print('''Escolha uma opção:
                                1 - Tentar novamente
                                2 - Cadastrar Usuário
                                ''')

                                try:
                                    escolha = int(input("Qual a sua escolha: "))
                                except ValueError:
                                    print("Valor invalido!")
                                    return

                                if escolha == 1:
                                    login()

                                elif escolha == 2:
                                    cad_user()

                                else:
                                    print("Opção invalida!")
                                    return

                else:
                    print("Usuário invalido!")
                    return


# tela de login do taskforge
# user tenta login caso nao consiga ou nao ache a conta roda o cadastro py para cadastrar no banco de dados
# dps de cadastrado roda novamente o login para efetuar o login com os cadastros do user referente
# por fim roda o menu.py
