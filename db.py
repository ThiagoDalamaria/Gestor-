import os
from decimal import Decimal
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error


load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", None),
    "charset": "utf8mb4"
}

def get_conn():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"033[91m❌ Erro ao conectar no banco: {e}\033[0m")
        return None

def criar_tabela_produtos():
    """Cria a tabela produtos se não existir."""
    sql = """
          CREATE TABLE IF NOT EXISTS produtos \
          ( \
              id \
              INT \
              AUTO_INCREMENT \
              PRIMARY \
              KEY, \
              nome \
              VARCHAR \
          ( \
              255 \
          ) NOT NULL,
              codigo VARCHAR \
          ( \
              13 \
          ) NOT NULL UNIQUE,
              preco DECIMAL \
          ( \
              10, \
              2 \
          ) NOT NULL,
              quantidade INT NOT NULL,
              criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) CHARACTER SET = utf8mb4; \
          """

    conn = get_conn()
    if not conn:
        return
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(f"\033[91m❌ Erro ao criar tabela: {e}\033[0m")
    finally:
        if cursor is not None:
            cursor.close()
        if conn.is_connected():
            conn.close()

def inserir_produto(nome: str, codigo: str, preco: Decimal, quantidade: int):
    """Insere produto. Retorna id inserido ou None em caso de erro."""
    sql = "INSERT INTO produtos (nome, codigo, preco, quantidade) VALUES (%s, %s, %s, %s)"
    conn = get_conn()
    if not conn:
        return None
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (nome, codigo, str(preco), quantidade))
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.IntegrityError as ie:
        #por exemplo: código duplicado (UNIQUE)
        raise ie
    except Error as e:
        raise e
    finally:
        if cursor is not None:
            cursor.close()
        if conn.is_connected():
            conn.close()

def listar_produto():
    """Retorna lista de dicts com os produtos."""
    sql = "SELECT id, nome, codigo, preco, quantidade, criado_em FROM produtos ORDER BY id"
    conn = get_conn()
    if not conn:
        return []
    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(f"\033[91m❌ Erro ao listar produtos: {e}\033[0m")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conn.is_connected():
            conn.close()

def buscar_por_nome(nome: str):
    """Busca produtos com nome case-insensitive. Retorna lista."""
    sql = "SELECT id, nome, codigo, preco, quantidade FROM produtos WHERE LOWER(nome) = LOWER(%s)"
    conn = get_conn()
    if not conn:
        return []
    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (nome,))
        return cursor.fetchall()
    except Error as e:
        print(f"\033[91m❌ Erro na busca por nome: {e}\033[0m")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conn.is_connected():
            conn.close()

def remover_por_id(produto_id: int):
    """Remove produto por id. Retorna número de linhas afetadas (0/1)."""
    sql = "DELETE FROM produtos WHERE id = %s"
    conn = get_conn()
    if not conn:
        return 0
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (produto_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(f"\033[91m❌ Erro ao remover produto: {e}\033[0m")
        return 0
    finally:
        if cursor is not None:
            cursor.close()
        if conn.is_connected():
            conn.close()
