from user.login import tela_login
from menu import menu_inicial


def main():
    usuario_id = tela_login()

    if usuario_id is not None:
        menu_inicial(usuario_id)


if __name__ == "__main__":
    main()