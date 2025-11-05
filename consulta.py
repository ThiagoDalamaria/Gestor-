from funções import linha_l
from db import listar_produto


def consulta_cadastro():
    linha_l()
    produto = listar_produto()
    if not produto:
        print("\033[93m❌ Não há produtos cadastrados.\033[0m")
        linha_l()
        return

    print("\nLista de Produtos:")
    for p in produto:
        # formata preço com 2 casas
        preco_fmt = f"{p['preco']:.2f}"
        print(f"{p['id']}. Nome: {p['nome']} | Código: {p['codigo']} | Preço: {preco_fmt} | Qtde: {p['quantidade']}")
    linha_l()
