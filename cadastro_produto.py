from funções import linha_l



linha_l()
print("Cadastro de Produto".center(30))
linha_l()

estoque = []
def cadastrar_produto():
        # -- Produto --
    while True:
        nome_produto = input("Nome do Produto: ").strip()
        if all(parte.isalpha() for parte in nome_produto.split()):
            nome_produto = nome_produto.title()
            break

        print("\033[91mErro: Nome inválido.\033[0m")
        linha_l()

        # -- Código do produto --
    while True:
        codigo_produto = input("Código do Produto: ")

        if not codigo_produto.isdigit():
            print("\033[91m❌ O código deve conter apenas números.\033[0m ")
        elif len(codigo_produto) == 0:
            print("\033[91m❌ O código não deve estar vazio.\033[0m ")
        elif len(codigo_produto) > 13:
            print("\033[91m❌ O código não pode ultrapassar dos 13 dígitos.\033[0m ")
        else:
            break
        linha_l()

        # -- Preço de Custo --
    while True:
        preco_custo_str = input("Preço de Custo: ").strip()
        preco_custo_str = preco_custo_str.replace(",", ".")

        try:
            preco_custo = float(preco_custo_str)
            if preco_custo > 0:
                break
            else:
                print("\033[93m⚠️  O valor precisa ser maior que zero.\033[0m ")

        except ValueError:
            print("\033[93m⚠️  Valor inválido! Digite apenas números, ex: 38.49 ")
            linha_l()

            # Quantidade de itens
    while True:
        quantidade_str =  input("Quantidade de produto: ")

        try:
            quantidade = int(quantidade_str)
            if quantidade >0:
                break
            else:
                print("\033[93m⚠️  O valor precisa ser maior que zero.\033[0m ")

        except ValueError:
            print("\033[93m⚠️  Valor inválido! Digite apenas números. ex: 2, 5, 19 ")
            linha_l()





while True:
        cadastrar_produto()
        break



