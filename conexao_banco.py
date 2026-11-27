import sqlite3

try:
    with sqlite3.connect("usuarios.db") as conexao_banco:
        cursor = conexao_banco.cursor()
except sqlite3.Error as e:
    print(f"Erro ao se conectar com o banco de dados: {e}")


tabela_dados = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT   
)
"""

conexao_banco.execute(tabela_dados)
print("Banco de dados e tabela criados!")



