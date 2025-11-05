from conexao import criar_conexao
from funções import linha_l



def cadastrar_produto():

    linha_l()
    print("Cadastro de Produto".center(30))
    linha_l()

        # -- Produto --
    while True:
        nome_produto = input("Nome do Produto: ").strip()
        if nome_produto and all(p.isalpha() for p in nome_produto.split()):
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

            # -- Quantidade de itens --
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


    # ---  Salvar no Banco ---
    conexao = None
    cursor = None
    try:
        conexao = criar_conexao()
        if not conexao:
            print("\033[91m❌ Falha ao conectar ao banco de dados.\033[0m")
            return

        cursor = conexao.cursor()
        query = """
            INSERT INTO produtos (nome, codigo, preco, quantidade)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nome_produto, codigo_produto, preco_custo, quantidade)
        cursor.execute(query, valores)
        conexao.commit()

        print(f"\033[92m✅ Produto '{nome_produto}' cadastrado com sucesso no banco de dados!\033[0m")
        linha_l()

    except Exception as e:
        print(f"\033[91m❌ Erro ao cadastrar produto: {e}\033[0m")
        linha_l()

    finally:
        # fecha cursor e conexão com checagem (evita referência antes de atribuir)
        try:
            if cursor is not None:
                cursor.close()
        except BaseException:
            pass

        try:
            if conexao is not None and hasattr(conexao, "is_connected") and conexao.is_connected():
                conexao.close()
        except BaseException:
            pass

