"""
Product module for Stock Management System
Handles all product-related operations (CRUD)
"""
import sqlite3
from datetime import datetime


class Produto:
    """Product management class"""
    
    def __init__(self, db):
        """Initialize with database connection"""
        self.db = db
    
    def cadastrar(self, codigo, nome, categoria, descricao, quantidade, preco_unitario):
        """Register a new product"""
        try:
            self.db.cursor.execute('''
                INSERT INTO produtos (codigo, nome, categoria, descricao, quantidade, preco_unitario)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (codigo, nome, categoria, descricao, quantidade, preco_unitario))
            self.db.conn.commit()
            
            # Register initial stock movement
            produto_id = self.db.cursor.lastrowid
            if quantidade > 0:
                self._registrar_movimentacao(produto_id, 'ENTRADA', quantidade, 'Estoque inicial')
            
            return True, "Produto cadastrado com sucesso!"
        except sqlite3.IntegrityError:
            return False, "Erro: Código do produto já existe!"
        except sqlite3.Error as e:
            return False, f"Erro ao cadastrar produto: {e}"
    
    def editar(self, produto_id, nome=None, categoria=None, descricao=None, preco_unitario=None):
        """Edit product information"""
        try:
            # Build dynamic update query
            updates = []
            params = []
            
            if nome is not None:
                updates.append("nome = ?")
                params.append(nome)
            if categoria is not None:
                updates.append("categoria = ?")
                params.append(categoria)
            if descricao is not None:
                updates.append("descricao = ?")
                params.append(descricao)
            if preco_unitario is not None:
                updates.append("preco_unitario = ?")
                params.append(preco_unitario)
            
            if not updates:
                return False, "Nenhuma informação para atualizar"
            
            updates.append("data_atualizacao = CURRENT_TIMESTAMP")
            params.append(produto_id)
            
            query = f"UPDATE produtos SET {', '.join(updates)} WHERE id = ?"
            self.db.cursor.execute(query, params)
            self.db.conn.commit()
            
            if self.db.cursor.rowcount > 0:
                return True, "Produto atualizado com sucesso!"
            else:
                return False, "Produto não encontrado!"
        except sqlite3.Error as e:
            return False, f"Erro ao atualizar produto: {e}"
    
    def excluir(self, produto_id):
        """Delete a product"""
        try:
            # Check if product exists
            self.db.cursor.execute("SELECT nome FROM produtos WHERE id = ?", (produto_id,))
            produto = self.db.cursor.fetchone()
            
            if not produto:
                return False, "Produto não encontrado!"
            
            # Delete related stock movements first
            self.db.cursor.execute("DELETE FROM movimentacoes WHERE produto_id = ?", (produto_id,))
            
            # Delete product
            self.db.cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            self.db.conn.commit()
            
            return True, f"Produto '{produto[0]}' excluído com sucesso!"
        except sqlite3.Error as e:
            return False, f"Erro ao excluir produto: {e}"
    
    def consultar_por_id(self, produto_id):
        """Query product by ID"""
        try:
            self.db.cursor.execute('''
                SELECT id, codigo, nome, categoria, descricao, quantidade, preco_unitario, 
                       data_cadastro, data_atualizacao
                FROM produtos WHERE id = ?
            ''', (produto_id,))
            return self.db.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Erro ao consultar produto: {e}")
            return None
    
    def consultar_por_codigo(self, codigo):
        """Query product by code"""
        try:
            self.db.cursor.execute('''
                SELECT id, codigo, nome, categoria, descricao, quantidade, preco_unitario, 
                       data_cadastro, data_atualizacao
                FROM produtos WHERE codigo = ?
            ''', (codigo,))
            return self.db.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Erro ao consultar produto: {e}")
            return None
    
    def consultar_por_nome(self, nome):
        """Query products by name (partial match)"""
        try:
            self.db.cursor.execute('''
                SELECT id, codigo, nome, categoria, descricao, quantidade, preco_unitario, 
                       data_cadastro, data_atualizacao
                FROM produtos WHERE nome LIKE ?
            ''', (f'%{nome}%',))
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao consultar produtos: {e}")
            return []
    
    def consultar_por_categoria(self, categoria):
        """Query products by category"""
        try:
            self.db.cursor.execute('''
                SELECT id, codigo, nome, categoria, descricao, quantidade, preco_unitario, 
                       data_cadastro, data_atualizacao
                FROM produtos WHERE categoria = ?
            ''', (categoria,))
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao consultar produtos: {e}")
            return []
    
    def listar_todos(self):
        """List all products"""
        try:
            self.db.cursor.execute('''
                SELECT id, codigo, nome, categoria, descricao, quantidade, preco_unitario, 
                       data_cadastro, data_atualizacao
                FROM produtos ORDER BY nome
            ''')
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao listar produtos: {e}")
            return []
    
    def entrada_estoque(self, produto_id, quantidade, observacao=""):
        """Register stock entry"""
        if quantidade <= 0:
            return False, "Quantidade deve ser maior que zero!"
        
        try:
            # Update stock
            self.db.cursor.execute('''
                UPDATE produtos SET quantidade = quantidade + ?, 
                       data_atualizacao = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (quantidade, produto_id))
            
            if self.db.cursor.rowcount == 0:
                return False, "Produto não encontrado!"
            
            # Register movement
            self._registrar_movimentacao(produto_id, 'ENTRADA', quantidade, observacao)
            self.db.conn.commit()
            
            return True, "Entrada de estoque registrada com sucesso!"
        except sqlite3.Error as e:
            return False, f"Erro ao registrar entrada: {e}"
    
    def saida_estoque(self, produto_id, quantidade, observacao=""):
        """Register stock exit"""
        if quantidade <= 0:
            return False, "Quantidade deve ser maior que zero!"
        
        try:
            # Check current stock
            self.db.cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (produto_id,))
            result = self.db.cursor.fetchone()
            
            if not result:
                return False, "Produto não encontrado!"
            
            estoque_atual = result[0]
            if estoque_atual < quantidade:
                return False, f"Estoque insuficiente! Disponível: {estoque_atual}"
            
            # Update stock
            self.db.cursor.execute('''
                UPDATE produtos SET quantidade = quantidade - ?, 
                       data_atualizacao = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (quantidade, produto_id))
            
            # Register movement
            self._registrar_movimentacao(produto_id, 'SAIDA', quantidade, observacao)
            self.db.conn.commit()
            
            return True, "Saída de estoque registrada com sucesso!"
        except sqlite3.Error as e:
            return False, f"Erro ao registrar saída: {e}"
    
    def _registrar_movimentacao(self, produto_id, tipo, quantidade, observacao):
        """Internal method to register stock movement"""
        self.db.cursor.execute('''
            INSERT INTO movimentacoes (produto_id, tipo, quantidade, observacao)
            VALUES (?, ?, ?, ?)
        ''', (produto_id, tipo, quantidade, observacao))
    
    def historico_movimentacoes(self, produto_id):
        """Get stock movement history for a product"""
        try:
            self.db.cursor.execute('''
                SELECT m.id, m.tipo, m.quantidade, m.observacao, m.data_movimentacao, p.nome
                FROM movimentacoes m
                JOIN produtos p ON m.produto_id = p.id
                WHERE m.produto_id = ?
                ORDER BY m.data_movimentacao DESC
            ''', (produto_id,))
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao consultar histórico: {e}")
            return []
