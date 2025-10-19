"""
Test script for Stock Management System
Tests all main functionalities
"""
import os
import sys
from database import Database
from produto import Produto


def test_database_initialization():
    """Test database creation and initialization"""
    print("\n🧪 Testando inicialização do banco de dados...")
    try:
        db = Database('test_estoque.db')
        assert db.conn is not None, "Conexão não estabelecida"
        assert db.cursor is not None, "Cursor não criado"
        
        # Check if tables exist
        db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in db.cursor.fetchall()]
        assert 'produtos' in tables, "Tabela produtos não criada"
        assert 'movimentacoes' in tables, "Tabela movimentacoes não criada"
        
        db.close()
        print("✅ Inicialização do banco de dados: SUCESSO")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def test_product_crud():
    """Test product CRUD operations"""
    print("\n🧪 Testando operações CRUD de produtos...")
    try:
        db = Database('test_estoque.db')
        produto = Produto(db)
        
        # Test CREATE
        print("  - Testando cadastro...")
        sucesso, msg = produto.cadastrar('TEST001', 'Produto Teste', 'Categoria Teste', 
                                         'Descrição teste', 10, 25.50)
        assert sucesso, f"Falha ao cadastrar: {msg}"
        print(f"    ✅ Cadastro: {msg}")
        
        # Test READ by code
        print("  - Testando consulta por código...")
        resultado = produto.consultar_por_codigo('TEST001')
        assert resultado is not None, "Produto não encontrado"
        assert resultado[1] == 'TEST001', "Código incorreto"
        assert resultado[2] == 'Produto Teste', "Nome incorreto"
        print(f"    ✅ Consulta: Produto encontrado - {resultado[2]}")
        
        produto_id = resultado[0]
        
        # Test UPDATE
        print("  - Testando edição...")
        sucesso, msg = produto.editar(produto_id, nome='Produto Teste Editado', preco_unitario=30.00)
        assert sucesso, f"Falha ao editar: {msg}"
        print(f"    ✅ Edição: {msg}")
        
        # Verify update
        resultado = produto.consultar_por_id(produto_id)
        assert resultado[2] == 'Produto Teste Editado', "Nome não foi atualizado"
        assert resultado[6] == 30.00, "Preço não foi atualizado"
        
        # Test DELETE
        print("  - Testando exclusão...")
        sucesso, msg = produto.excluir(produto_id)
        assert sucesso, f"Falha ao excluir: {msg}"
        print(f"    ✅ Exclusão: {msg}")
        
        # Verify deletion
        resultado = produto.consultar_por_id(produto_id)
        assert resultado is None, "Produto não foi excluído"
        
        db.close()
        print("✅ Operações CRUD: SUCESSO")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def test_stock_movements():
    """Test stock entry and exit operations"""
    print("\n🧪 Testando movimentações de estoque...")
    try:
        db = Database('test_estoque.db')
        produto = Produto(db)
        
        # Create a test product
        sucesso, msg = produto.cadastrar('TEST002', 'Produto Estoque', 'Teste', 
                                         'Teste de estoque', 100, 10.00)
        assert sucesso, f"Falha ao cadastrar produto: {msg}"
        
        resultado = produto.consultar_por_codigo('TEST002')
        produto_id = resultado[0]
        estoque_inicial = resultado[5]
        
        # Test stock entry
        print("  - Testando entrada de estoque...")
        sucesso, msg = produto.entrada_estoque(produto_id, 50, "Entrada teste")
        assert sucesso, f"Falha na entrada: {msg}"
        print(f"    ✅ Entrada: {msg}")
        
        # Verify stock increase
        resultado = produto.consultar_por_id(produto_id)
        assert resultado[5] == estoque_inicial + 50, "Estoque não foi incrementado corretamente"
        print(f"    ✅ Estoque após entrada: {resultado[5]}")
        
        # Test stock exit
        print("  - Testando saída de estoque...")
        sucesso, msg = produto.saida_estoque(produto_id, 30, "Saída teste")
        assert sucesso, f"Falha na saída: {msg}"
        print(f"    ✅ Saída: {msg}")
        
        # Verify stock decrease
        resultado = produto.consultar_por_id(produto_id)
        assert resultado[5] == estoque_inicial + 50 - 30, "Estoque não foi decrementado corretamente"
        print(f"    ✅ Estoque após saída: {resultado[5]}")
        
        # Test insufficient stock
        print("  - Testando saída com estoque insuficiente...")
        sucesso, msg = produto.saida_estoque(produto_id, 1000, "Saída inválida")
        assert not sucesso, "Deveria falhar com estoque insuficiente"
        print(f"    ✅ Validação de estoque: {msg}")
        
        # Test movement history
        print("  - Testando histórico de movimentações...")
        historico = produto.historico_movimentacoes(produto_id)
        assert len(historico) == 3, f"Esperado 3 movimentações, encontrado {len(historico)}"
        print(f"    ✅ Histórico: {len(historico)} movimentações registradas")
        
        db.close()
        print("✅ Movimentações de estoque: SUCESSO")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def test_search_functionality():
    """Test product search functionality"""
    print("\n🧪 Testando funcionalidades de busca...")
    try:
        db = Database('test_estoque.db')
        produto = Produto(db)
        
        # Create multiple test products
        produto.cadastrar('SEARCH001', 'Notebook Dell', 'Eletrônicos', 'Notebook', 5, 3000.00)
        produto.cadastrar('SEARCH002', 'Notebook Lenovo', 'Eletrônicos', 'Notebook', 3, 2500.00)
        produto.cadastrar('SEARCH003', 'Mouse Logitech', 'Acessórios', 'Mouse', 20, 50.00)
        
        # Test search by name
        print("  - Testando busca por nome...")
        resultados = produto.consultar_por_nome('Notebook')
        assert len(resultados) == 2, f"Esperado 2 notebooks, encontrado {len(resultados)}"
        print(f"    ✅ Busca por nome: {len(resultados)} produtos encontrados")
        
        # Test search by category
        print("  - Testando busca por categoria...")
        resultados = produto.consultar_por_categoria('Eletrônicos')
        assert len(resultados) == 2, f"Esperado 2 eletrônicos, encontrado {len(resultados)}"
        print(f"    ✅ Busca por categoria: {len(resultados)} produtos encontrados")
        
        # Test list all
        print("  - Testando listagem de todos os produtos...")
        todos = produto.listar_todos()
        assert len(todos) >= 3, f"Esperado pelo menos 3 produtos, encontrado {len(todos)}"
        print(f"    ✅ Listagem: {len(todos)} produtos no total")
        
        db.close()
        print("✅ Funcionalidades de busca: SUCESSO")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def cleanup():
    """Remove test database"""
    try:
        if os.path.exists('test_estoque.db'):
            os.remove('test_estoque.db')
            print("\n🧹 Arquivo de teste removido")
    except Exception as e:
        print(f"\n⚠️  Erro ao remover arquivo de teste: {e}")


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("TESTES DO SISTEMA DE GERENCIAMENTO DE ESTOQUE".center(60))
    print("="*60)
    
    tests = [
        test_database_initialization,
        test_product_crud,
        test_stock_movements,
        test_search_functionality
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\n❌ Erro inesperado em {test.__name__}: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print("RESUMO DOS TESTES".center(60))
    print("="*60)
    print(f"✅ Testes passados: {passed}")
    print(f"❌ Testes falhos: {failed}")
    print(f"📊 Total: {passed + failed}")
    print("="*60 + "\n")
    
    cleanup()
    
    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
