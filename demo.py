"""
Demonstration script for Stock Management System
Shows all main features working
"""
from database import Database
from produto import Produto


def print_section(title):
    """Print a section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def format_product(produto):
    """Format product data for display"""
    return f"ID: {produto[0]} | Código: {produto[1]} | Nome: {produto[2]} | " \
           f"Categoria: {produto[3]} | Qtd: {produto[5]} | Preço: R$ {produto[6]:.2f}"


def main():
    """Run demonstration"""
    print("\n" + "*"*70)
    print("  🧾 DEMONSTRAÇÃO DO SISTEMA DE GERENCIAMENTO DE ESTOQUE")
    print("*"*70)
    
    # Initialize
    print("\n📦 Inicializando sistema...")
    db = Database('demo_estoque.db')
    produto = Produto(db)
    print("✅ Sistema inicializado!")
    
    # 1. CADASTRAR PRODUTOS
    print_section("1️⃣  CADASTRAR PRODUTOS")
    
    produtos_demo = [
        ('NB001', 'Notebook Dell Inspiron', 'Eletrônicos', 'Notebook 15.6 polegadas', 5, 3500.00),
        ('NB002', 'Notebook Lenovo', 'Eletrônicos', 'Notebook 14 polegadas', 3, 2800.00),
        ('MS001', 'Mouse Logitech', 'Acessórios', 'Mouse wireless', 20, 89.90),
        ('KB001', 'Teclado Mecânico', 'Acessórios', 'Teclado RGB', 10, 350.00),
        ('MON01', 'Monitor LG 24"', 'Eletrônicos', 'Monitor Full HD', 8, 800.00),
    ]
    
    for codigo, nome, categoria, descricao, qtd, preco in produtos_demo:
        sucesso, msg = produto.cadastrar(codigo, nome, categoria, descricao, qtd, preco)
        print(f"  {'✅' if sucesso else '❌'} {nome}: {msg}")
    
    # 2. LISTAR TODOS OS PRODUTOS
    print_section("2️⃣  LISTAR TODOS OS PRODUTOS")
    todos = produto.listar_todos()
    for p in todos:
        print(f"  {format_product(p)}")
    print(f"\n  📊 Total: {len(todos)} produtos cadastrados")
    
    # 3. CONSULTAR POR NOME
    print_section("3️⃣  CONSULTAR PRODUTOS POR NOME (busca: 'Notebook')")
    resultados = produto.consultar_por_nome('Notebook')
    for p in resultados:
        print(f"  {format_product(p)}")
    print(f"\n  🔍 Encontrados: {len(resultados)} produtos")
    
    # 4. CONSULTAR POR CATEGORIA
    print_section("4️⃣  CONSULTAR PRODUTOS POR CATEGORIA (Acessórios)")
    resultados = produto.consultar_por_categoria('Acessórios')
    for p in resultados:
        print(f"  {format_product(p)}")
    print(f"\n  🔍 Encontrados: {len(resultados)} produtos")
    
    # 5. CONSULTAR POR CÓDIGO
    print_section("5️⃣  CONSULTAR PRODUTO POR CÓDIGO (NB001)")
    resultado = produto.consultar_por_codigo('NB001')
    if resultado:
        print(f"  {format_product(resultado)}")
    
    # 6. EDITAR PRODUTO
    print_section("6️⃣  EDITAR PRODUTO")
    resultado = produto.consultar_por_codigo('MS001')
    produto_id = resultado[0]
    print(f"  Antes: {format_product(resultado)}")
    
    sucesso, msg = produto.editar(produto_id, nome='Mouse Logitech MX Master', preco_unitario=199.90)
    print(f"  {msg}")
    
    resultado_atualizado = produto.consultar_por_id(produto_id)
    print(f"  Depois: {format_product(resultado_atualizado)}")
    
    # 7. ENTRADA DE ESTOQUE
    print_section("7️⃣  ENTRADA DE ESTOQUE")
    resultado = produto.consultar_por_codigo('NB001')
    produto_id = resultado[0]
    print(f"  Produto: {resultado[2]}")
    print(f"  Estoque Atual: {resultado[5]}")
    
    sucesso, msg = produto.entrada_estoque(produto_id, 10, "Reposição de estoque")
    print(f"  {msg}")
    
    resultado_atualizado = produto.consultar_por_id(produto_id)
    print(f"  Novo Estoque: {resultado_atualizado[5]}")
    
    # 8. SAÍDA DE ESTOQUE
    print_section("8️⃣  SAÍDA DE ESTOQUE")
    print(f"  Produto: {resultado_atualizado[2]}")
    print(f"  Estoque Atual: {resultado_atualizado[5]}")
    
    sucesso, msg = produto.saida_estoque(produto_id, 7, "Venda para cliente")
    print(f"  {msg}")
    
    resultado_atualizado = produto.consultar_por_id(produto_id)
    print(f"  Novo Estoque: {resultado_atualizado[5]}")
    
    # 9. HISTÓRICO DE MOVIMENTAÇÕES
    print_section("9️⃣  HISTÓRICO DE MOVIMENTAÇÕES")
    print(f"  Produto: {resultado_atualizado[2]} (ID: {produto_id})")
    historico = produto.historico_movimentacoes(produto_id)
    print(f"\n  {'Tipo':<10} {'Qtd':<8} {'Observação':<30} {'Data'}")
    print("  " + "-"*66)
    for mov in historico:
        print(f"  {mov[1]:<10} {mov[2]:<8} {mov[3] or '-':<30} {mov[4]}")
    print(f"\n  📋 Total: {len(historico)} movimentações")
    
    # 10. EXCLUIR PRODUTO
    print_section("🔟 EXCLUIR PRODUTO")
    resultado = produto.consultar_por_codigo('KB001')
    produto_id = resultado[0]
    print(f"  Produto a ser excluído: {resultado[2]} (ID: {produto_id})")
    
    sucesso, msg = produto.excluir(produto_id)
    print(f"  {msg}")
    
    # Verificar exclusão
    resultado_deletado = produto.consultar_por_id(produto_id)
    if resultado_deletado is None:
        print(f"  ✅ Produto foi removido com sucesso do sistema")
    
    # RESUMO FINAL
    print_section("📊 RESUMO FINAL")
    todos = produto.listar_todos()
    print(f"  Total de produtos cadastrados: {len(todos)}")
    
    estoque_total = sum(p[5] for p in todos)
    valor_total = sum(p[5] * p[6] for p in todos)
    
    print(f"  Total de itens em estoque: {estoque_total}")
    print(f"  Valor total do estoque: R$ {valor_total:,.2f}")
    
    # Cleanup
    db.close()
    print("\n✅ Demonstração concluída!")
    print("*"*70 + "\n")
    
    # Remove demo database
    import os
    if os.path.exists('demo_estoque.db'):
        os.remove('demo_estoque.db')
        print("🧹 Banco de dados de demonstração removido\n")


if __name__ == "__main__":
    main()
