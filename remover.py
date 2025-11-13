from funções import linha_l
from db import buscar_por_nome, remover_por_id

def remover_produto():
    linha_l()
    nome = input("Digite o nome do produto a remover: ").strip()
    if not nome:
        print("\033[93m⚠️ Nome vazio. Operação cancelada.\033[0m")
        linha_l()
        return

    encontrados = buscar_por_nome(nome)
    if not encontrados:
        print(f"\033[93m⚠️ Produto '{nome}' não encontrado.\033[0m")
        linha_l()
        return


    if len(encontrados) > 1:
        print("Foram encontrados vários produtos com esse nome:")
        for p in encontrados:
            print(f"{p['id']}: {p['nome']} — Código: {p['codigo']} — Qtde: {p['quantidade']}")
        linha_l()
        try:
            escolha = int(input("Digite o id do produto que deseja remover: ").strip())
        except ValueError:
            print("\033[93m⚠️ Entrada inválida. Operação cancelada.\033[0m")
            linha_l()
            return

        removido = remover_por_id(escolha)
        if removido:
            print("\033[92m🚮 Produto removido com sucesso!\033[0m")
        else:
            print("\033[93m⚠️ Nenhum produto removido (id inválido).\033[0m")
        linha_l()
        return


    p = encontrados[0]
    confirma = input(f"Confirma remover '{p['nome']}' (código {p['codigo']})? [s/N]: ").strip().lower()
    if confirma != "s":
        print("Operação cancelada.")
        linha_l()
        return

    removido = remover_por_id(p['id'])
    if removido:
        print("\033[92m🚮 Produto removido com sucesso!\033[0m")
    else:
        print("\033[91m❌ Falha ao remover produto.\033[0m")
    linha_l()
