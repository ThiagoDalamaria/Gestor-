from datetime import datetime
from cadastro import cadastrar_produto
from remover import remover_produto
from consulta import consulta_cadastro
from funções import linha_l
from atualizar import atualizar_produto_menu


while True:
    agora = datetime.now().strftime("%d/%m %H:%M")

    linha_l()
    print(f"{'Cadastro de Produto 📦':<30}{agora:>28}")
    linha_l()

    print("1️⃣  -  Cadastrar Produto ")
    print("2️⃣  -  Remover Produto ")
    print("3️⃣  -  Lista cadastrada ")
    print("4️⃣  -  Atualizar cadastro ")
    print("5️⃣  -  Encerrando programa ")
    linha_l()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        remover_produto()
    elif opcao == "3":
        consulta_cadastro()
    elif opcao == "4":
        print("Encerrando... ")
        break
    else:
        print("❌ Opção inválida!")
