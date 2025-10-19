"""
Main interface for Stock Management System
Provides menu-based interaction for users
"""
import os
from database import Database
from produto import Produto


def limpar_tela():
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu_principal():
    """Display main menu"""
    print("\n" + "="*60)
    print("🧾 SISTEMA DE GERENCIAMENTO DE ESTOQUE".center(60))
    print("="*60)
    print("\n[1] Cadastrar Produto")
    print("[2] Editar Produto")
    print("[3] Excluir Produto")
    print("[4] Consultar Produtos")
    print("[5] Entrada de Estoque")
    print("[6] Saída de Estoque")
    print("[7] Histórico de Movimentações")
    print("[8] Listar Todos os Produtos")
    print("[0] Sair")
    print("\n" + "-"*60)


def cadastrar_produto(produto):
    """Product registration interface"""
    print("\n" + "="*60)
    print("CADASTRAR NOVO PRODUTO".center(60))
    print("="*60 + "\n")
    
    try:
        codigo = input("Código do Produto: ").strip()
        if not codigo:
            print("❌ Código não pode estar vazio!")
            return
        
        nome = input("Nome: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        categoria = input("Categoria: ").strip()
        descricao = input("Descrição: ").strip()
        
        quantidade = input("Quantidade Inicial (0 se vazio): ").strip()
        quantidade = int(quantidade) if quantidade else 0
        
        preco = input("Preço Unitário (0.00 se vazio): ").strip()
        preco = float(preco) if preco else 0.0
        
        sucesso, mensagem = produto.cadastrar(codigo, nome, categoria, descricao, quantidade, preco)
        
        if sucesso:
            print(f"\n✅ {mensagem}")
        else:
            print(f"\n❌ {mensagem}")
    
    except ValueError:
        print("\n❌ Erro: Valor numérico inválido!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def editar_produto(produto):
    """Product editing interface"""
    print("\n" + "="*60)
    print("EDITAR PRODUTO".center(60))
    print("="*60 + "\n")
    
    try:
        produto_id = input("ID do Produto: ").strip()
        if not produto_id:
            print("❌ ID não pode estar vazio!")
            return
        
        produto_id = int(produto_id)
        
        # Get current product data
        dados = produto.consultar_por_id(produto_id)
        if not dados:
            print(f"\n❌ Produto ID {produto_id} não encontrado!")
            return
        
        print(f"\nProduto Atual: {dados[2]} (Código: {dados[1]})")
        print("\nDeixe em branco para manter o valor atual\n")
        
        nome = input(f"Nome [{dados[2]}]: ").strip()
        categoria = input(f"Categoria [{dados[3]}]: ").strip()
        descricao = input(f"Descrição [{dados[4]}]: ").strip()
        preco = input(f"Preço Unitário [{dados[6]}]: ").strip()
        
        # Prepare update parameters
        kwargs = {}
        if nome:
            kwargs['nome'] = nome
        if categoria:
            kwargs['categoria'] = categoria
        if descricao:
            kwargs['descricao'] = descricao
        if preco:
            kwargs['preco_unitario'] = float(preco)
        
        if not kwargs:
            print("\n⚠️  Nenhuma alteração realizada!")
            return
        
        sucesso, mensagem = produto.editar(produto_id, **kwargs)
        
        if sucesso:
            print(f"\n✅ {mensagem}")
        else:
            print(f"\n❌ {mensagem}")
    
    except ValueError:
        print("\n❌ Erro: Valor inválido!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def excluir_produto(produto):
    """Product deletion interface"""
    print("\n" + "="*60)
    print("EXCLUIR PRODUTO".center(60))
    print("="*60 + "\n")
    
    try:
        produto_id = input("ID do Produto: ").strip()
        if not produto_id:
            print("❌ ID não pode estar vazio!")
            return
        
        produto_id = int(produto_id)
        
        # Show product details before deletion
        dados = produto.consultar_por_id(produto_id)
        if not dados:
            print(f"\n❌ Produto ID {produto_id} não encontrado!")
            return
        
        print(f"\nProduto: {dados[2]} (Código: {dados[1]})")
        print(f"Categoria: {dados[3]}")
        print(f"Quantidade em Estoque: {dados[5]}")
        
        confirmacao = input("\n⚠️  Confirma exclusão? (S/N): ").strip().upper()
        
        if confirmacao == 'S':
            sucesso, mensagem = produto.excluir(produto_id)
            if sucesso:
                print(f"\n✅ {mensagem}")
            else:
                print(f"\n❌ {mensagem}")
        else:
            print("\n⚠️  Operação cancelada!")
    
    except ValueError:
        print("\n❌ Erro: ID inválido!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def consultar_produtos(produto):
    """Product query interface"""
    print("\n" + "="*60)
    print("CONSULTAR PRODUTOS".center(60))
    print("="*60 + "\n")
    print("[1] Por Código")
    print("[2] Por Nome")
    print("[3] Por Categoria")
    print("\nOpção: ", end="")
    
    opcao = input().strip()
    
    if opcao == '1':
        codigo = input("\nCódigo: ").strip()
        resultado = produto.consultar_por_codigo(codigo)
        if resultado:
            exibir_produto(resultado)
        else:
            print("\n❌ Produto não encontrado!")
    
    elif opcao == '2':
        nome = input("\nNome (parcial): ").strip()
        resultados = produto.consultar_por_nome(nome)
        if resultados:
            exibir_lista_produtos(resultados)
        else:
            print("\n❌ Nenhum produto encontrado!")
    
    elif opcao == '3':
        categoria = input("\nCategoria: ").strip()
        resultados = produto.consultar_por_categoria(categoria)
        if resultados:
            exibir_lista_produtos(resultados)
        else:
            print("\n❌ Nenhum produto encontrado nesta categoria!")
    
    else:
        print("\n❌ Opção inválida!")


def exibir_produto(dados):
    """Display single product details"""
    print("\n" + "-"*60)
    print(f"ID: {dados[0]}")
    print(f"Código: {dados[1]}")
    print(f"Nome: {dados[2]}")
    print(f"Categoria: {dados[3]}")
    print(f"Descrição: {dados[4]}")
    print(f"Quantidade: {dados[5]}")
    print(f"Preço Unitário: R$ {dados[6]:.2f}")
    print(f"Cadastrado em: {dados[7]}")
    print(f"Última atualização: {dados[8]}")
    print("-"*60)


def exibir_lista_produtos(produtos):
    """Display list of products"""
    print("\n" + "="*100)
    print(f"{'ID':<5} {'Código':<15} {'Nome':<30} {'Categoria':<15} {'Qtd':<8} {'Preço':<10}")
    print("="*100)
    
    for p in produtos:
        print(f"{p[0]:<5} {p[1]:<15} {p[2]:<30} {p[3] or '-':<15} {p[5]:<8} R$ {p[6]:<8.2f}")
    
    print("="*100)
    print(f"Total: {len(produtos)} produto(s)")


def entrada_estoque(produto):
    """Stock entry interface"""
    print("\n" + "="*60)
    print("ENTRADA DE ESTOQUE".center(60))
    print("="*60 + "\n")
    
    try:
        produto_id = input("ID do Produto: ").strip()
        if not produto_id:
            print("❌ ID não pode estar vazio!")
            return
        
        produto_id = int(produto_id)
        
        # Show product info
        dados = produto.consultar_por_id(produto_id)
        if not dados:
            print(f"\n❌ Produto ID {produto_id} não encontrado!")
            return
        
        print(f"\nProduto: {dados[2]}")
        print(f"Estoque Atual: {dados[5]}")
        
        quantidade = input("\nQuantidade para Entrada: ").strip()
        if not quantidade:
            print("❌ Quantidade não pode estar vazia!")
            return
        
        quantidade = int(quantidade)
        observacao = input("Observação (opcional): ").strip()
        
        sucesso, mensagem = produto.entrada_estoque(produto_id, quantidade, observacao)
        
        if sucesso:
            print(f"\n✅ {mensagem}")
            # Show updated stock
            dados_atualizados = produto.consultar_por_id(produto_id)
            print(f"Novo Estoque: {dados_atualizados[5]}")
        else:
            print(f"\n❌ {mensagem}")
    
    except ValueError:
        print("\n❌ Erro: Valor inválido!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def saida_estoque(produto):
    """Stock exit interface"""
    print("\n" + "="*60)
    print("SAÍDA DE ESTOQUE".center(60))
    print("="*60 + "\n")
    
    try:
        produto_id = input("ID do Produto: ").strip()
        if not produto_id:
            print("❌ ID não pode estar vazio!")
            return
        
        produto_id = int(produto_id)
        
        # Show product info
        dados = produto.consultar_por_id(produto_id)
        if not dados:
            print(f"\n❌ Produto ID {produto_id} não encontrado!")
            return
        
        print(f"\nProduto: {dados[2]}")
        print(f"Estoque Atual: {dados[5]}")
        
        quantidade = input("\nQuantidade para Saída: ").strip()
        if not quantidade:
            print("❌ Quantidade não pode estar vazia!")
            return
        
        quantidade = int(quantidade)
        observacao = input("Observação (opcional): ").strip()
        
        sucesso, mensagem = produto.saida_estoque(produto_id, quantidade, observacao)
        
        if sucesso:
            print(f"\n✅ {mensagem}")
            # Show updated stock
            dados_atualizados = produto.consultar_por_id(produto_id)
            print(f"Novo Estoque: {dados_atualizados[5]}")
        else:
            print(f"\n❌ {mensagem}")
    
    except ValueError:
        print("\n❌ Erro: Valor inválido!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def historico_movimentacoes(produto):
    """Stock movement history interface"""
    print("\n" + "="*60)
    print("HISTÓRICO DE MOVIMENTAÇÕES".center(60))
    print("="*60 + "\n")
    
    try:
        produto_id = input("ID do Produto: ").strip()
        if not produto_id:
            print("❌ ID não pode estar vazio!")
            return
        
        produto_id = int(produto_id)
        
        # Show product info
        dados = produto.consultar_por_id(produto_id)
        if not dados:
            print(f"\n❌ Produto ID {produto_id} não encontrado!")
            return
        
        print(f"\nProduto: {dados[2]} (Código: {dados[1]})")
        print(f"Estoque Atual: {dados[5]}\n")
        
        movimentacoes = produto.historico_movimentacoes(produto_id)
        
        if movimentacoes:
            print("="*100)
            print(f"{'ID':<5} {'Tipo':<10} {'Qtd':<8} {'Observação':<40} {'Data':<25}")
            print("="*100)
            
            for mov in movimentacoes:
                print(f"{mov[0]:<5} {mov[1]:<10} {mov[2]:<8} {mov[3] or '-':<40} {mov[4]:<25}")
            
            print("="*100)
            print(f"Total: {len(movimentacoes)} movimentação(ões)")
        else:
            print("ℹ️  Nenhuma movimentação registrada para este produto.")
    
    except ValueError:
        print("\n❌ Erro: ID inválido!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def listar_todos_produtos(produto):
    """List all products interface"""
    print("\n" + "="*60)
    print("TODOS OS PRODUTOS".center(60))
    print("="*60)
    
    produtos = produto.listar_todos()
    
    if produtos:
        exibir_lista_produtos(produtos)
    else:
        print("\nℹ️  Nenhum produto cadastrado.")


def main():
    """Main application entry point"""
    print("\n🔄 Inicializando sistema...")
    
    # Initialize database
    db = Database()
    produto = Produto(db)
    
    print("✅ Sistema pronto!")
    
    try:
        while True:
            exibir_menu_principal()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                cadastrar_produto(produto)
            elif opcao == '2':
                editar_produto(produto)
            elif opcao == '3':
                excluir_produto(produto)
            elif opcao == '4':
                consultar_produtos(produto)
            elif opcao == '5':
                entrada_estoque(produto)
            elif opcao == '6':
                saida_estoque(produto)
            elif opcao == '7':
                historico_movimentacoes(produto)
            elif opcao == '8':
                listar_todos_produtos(produto)
            elif opcao == '0':
                print("\n👋 Encerrando sistema...")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            input("\nPressione ENTER para continuar...")
    
    finally:
        db.close()
        print("✅ Banco de dados fechado. Até logo!\n")


if __name__ == "__main__":
    main()
