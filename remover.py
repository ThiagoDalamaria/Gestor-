from funções import linha_l
from cadastro import estoque


# -- Remover cadastro --
def remover_produto():
    if not estoque:
        print("❌  Nenhum cadastro para remover.  ")
        return

    nome_produto = input("Digite o nome que você gostaria de remover do cadastro: ").strip()
    encontrado = False

    for lista_produto in estoque:
        if lista_produto ["Nome do Produto"].lower == nome_produto.lower():
            estoque.remove(nome_produto)
            print(f"🚮  Cadastro {nome_produto} foi removido com sucesso! ")
            encontrado = True
            linha_l()
            break
        if not encontrado:
            print(f"⚠️  Cliente {nome_produto} não foi encontrado. ")
