"""
Database module for Stock Management System
Handles database connection and initialization
"""
import sqlite3
from datetime import datetime


class Database:
    """Database handler for the stock management system"""
    
    def __init__(self, db_name='estoque.db'):
        """Initialize database connection"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Establish database connection"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
    
    def create_tables(self):
        """Create necessary tables if they don't exist"""
        try:
            # Products table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo VARCHAR(50) UNIQUE NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    descricao TEXT,
                    quantidade INTEGER DEFAULT 0,
                    preco_unitario REAL DEFAULT 0.0,
                    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Stock movements table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS movimentacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto_id INTEGER NOT NULL,
                    tipo VARCHAR(20) NOT NULL,
                    quantidade INTEGER NOT NULL,
                    observacao TEXT,
                    data_movimentacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (produto_id) REFERENCES produtos (id)
                )
            ''')
            
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
