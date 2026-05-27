from funções import linha_l
from db import buscar_por_nome, atualizar_produto

#Atualizar lista de produtos
def atualizar_produto_menu():
    linha_l()
    nome = input("Digite o nome do produto para alterar: ").strip()

    encontrados = buscar_por_nome(nome)

    if not encontrados:
        print("\033[93m⚠️ Produto não encontrado.\033[0m")
        return

    # se tiver mais de um, escolher
    if len(encontrados) >1:
        print("Vários produtos encontrados: ")
        for p in encontrados:
            print(f"{p['id']} - {p['nome']} - {p['codigo']}")

        produto_id = int(input("Digite o ID do produto: "))
        produto = next((p for p in encontrados if p ['id'] == produto_id), None)
    else:
        produto = encontrados[0]

    if not produto:
        print("ID inválido.")
        return

    print("\nDeixe vazio para manter o valor atual.\n")

    novo_nome = input(f"Nome ({produto['nome']}): ").strip() or produto['nome']
    novo_codigo = input(f"Código ({produto['codigo']}): ").strip() or produto['codigo']

    try:
        novo_preco = input(f"Preço ({produto['preco']}): ").strip()
        novo_preco = float(novo_preco) if novo_preco else produto['preco']

        nova_qtd = input(f"Quantidade ({produto['quantidade']}): ").strip()
        nova_qtd = int(nova_qtd) if nova_qtd else produto['quantidade']

    except ValueError:
        print("❌ Valores inválidos.")
        return

    resultado = atualizar_produto(
        produto['id'],
        novo_nome,
        novo_codigo,
        novo_preco,
        nova_qtd
    )

    if resultado:
        print("\033[92m✅ Produto atualizado com sucesso!\033[0m")
    else:
        print("\033[91m❌ Falha ao atualizar produto.\033[0m")
