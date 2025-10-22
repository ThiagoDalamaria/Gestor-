print("-" * 30)
print("Cadastro de Produto".center(30))
print("-" * 30)

estoque = []
def cadastrar_produto():
        # -- Produto --
    while True:
        nome_produto = input("Nome do Produto: ").strip()

        if all(parte.isalpha() for parte in nome_produto.split()):
            nome_produto = nome_produto.title()

            break
        print("\033[91mErro: Nome inválido.\033[0m")
    print(f"esse produto você cadastrou {nome_produto}")


        #codigo_produto = input("Código do Produto: ")
        #preco_entrada = input("Preço de Custo: ")
        #quantidade =  input("Quantidade: ")

print("-" * 30)

while True:
        cadastrar_produto()
        break
