from funções import linha_l
from cadastro import estoque


def consulta_cadastro():
    if not estoque:
        print("❌ Não há nenhum cliente cadastrado. ")
        linha_l()

    else:
        print("\n Lista de Produtos: ")
        for i, produto in enumerate(estoque,1):
            print(f"{i}. Nome: {produto['nome']}, Código: {produto['codigo']}, "
                  f"Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            linha_l()
