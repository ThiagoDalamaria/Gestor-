import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


load_dotenv()

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            datebase=os.getenv("DB_NAME")
        )

        if conexao.is_connected():
            print("✅  Conexão com o banco de dados estabelecida com sucesso! ")
            return conexao

    except Error as e:
        print(f"❌  Erro ao conectar ao banco de dados: ")
        return None

    return None
