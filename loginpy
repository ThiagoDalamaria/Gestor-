from datetime import datetime
from funções import linha_l
from db import buscar_usuario



def realizar_login():

    tentativas = 3

    while tentativas > 0:

        agora = datetime.now().strftime("%d/%m/%Y %H:%M")

        print("\n" *5)

        linha_l()
        print(f"{'Sistema de Estoque 📦':<35}{agora:>23}")
        linha_l()

        print("\n")
        print("🔒 LOGIN 🔒".center(60))
        print("\n")

        usuario = input(" " *20 + "Usuário: ").strip()
        senha = input(" " * 20 + "Senha: ").strip()

        dados = buscar_usuario(usuario)

        if dados and senha == dados["senha"]:
            print("\n")
            print(f"\033[92m{'✅ Login realizado com sucesso!':^60}\033[0m")
            return True

        tentativas -= 1

        print("\n")

        if tentativas > 0:
            print(
                f"\033[91m{'❌ Usuário ou senha inválido':^60}\033[0m"
            )
            print(
                f"\033[91m{'Tentativas restantes: ' +str(tentativas):^60}\033[0m"
            )

            input("\nPressione ENTER para tentar novamente...")

        print("\n")
    print(f"\033[91m{'🔒 Acesso bloqueado':^60}\033[0m")

    return False
