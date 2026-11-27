import sqlite3  # Biblioteca usada para trabalhar com bancos SQLite


def inserir_dados(nome, email, telefone):
    conexao_banco = sqlite3.connect("usuarios.db") # Cria uma conexão com o banco de dados
    cursor = conexao_banco.cursor() # Cria um cursor para executar comandos SQL

    # Comando SQL responsável por inserir um novo usuário
    inserir_comandos = "INSERT INTO usuarios (nome, email, telefone) VALUES (?,?,?)"

    try:
        cursor.execute(inserir_comandos, (nome, email, telefone))  # Executa o comando SQL substituindo os ? Pelos valores recebidos
        conexao_banco.commit() # Salva as alterações de forma permanente no banco
        return True # Retorna True indicando que o cadastro foi realizado com sucesso
    except sqlite3.IntegrityError: # Retorna False caso aconteça erro de integridade # Exemplo: email duplicado
        return False
    finally:  # Fecha a conexão independentemente de sucesso ou erro
        conexao_banco.close()


def buscar_usuario_por_id(id_usuario):
    conexao_banco = sqlite3.connect("usuarios.db") # Cria a conexão com o banco
    cursor = conexao_banco.cursor()  # Cria um cursor para executar comandos SQL

    buscar_usuario = "SELECT * FROM usuarios WHERE id = ?" # Comando SQL que procura um usuário pelo ID

    try:
        cursor.execute(buscar_usuario, (id_usuario,)) # Executa a consulta substituindo o ? Pelo valor de id_usuario
        usuarios = cursor.fetchone() # Busca apenas um registro da tabela
        return usuarios # Retorna os dados encontrados # Se não encontrar nenhum usuário, retorna None
    except sqlite3.OperationalError:  # Retorna False caso ocorra erro na consulta
        return False
    finally:
        conexao_banco.close() # Fecha a conexão


def ler_todos_usuarios():
    conexao_banco = sqlite3.connect("usuarios.db")
    cursor = conexao_banco.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios")  # Busca todos os registros da tabela usuarios
        todos_usuarios = cursor.fetchall() # Armazena todos os usuários encontrados
        return todos_usuarios  # Retorna uma lista contendo todos os usuários
    except sqlite3.OperationalError:
        return False  # Retorna False caso ocorra erro na consulta
    finally:
        conexao_banco.close()  # Fecha a conexão com o banco


def atualizar_os_dados(id_usuario, nome, email, telefone):
    conexao_banco = sqlite3.connect("usuarios.db")
    cursor = conexao_banco.cursor() # Cria cursor para executar SQL

    # Comando SQL responsável por atualizar um usuário existente
    comando_atualizar = "UPDATE usuarios SET nome = ?, email = ?, telefone = ? WHERE id = ?"

    try:
        cursor.execute(comando_atualizar,(nome, email, telefone, id_usuario))
        conexao_banco.commit() # Salva as alterações realizadas
        return True # Retorna True indicando que a atualização foi executada
    except sqlite3.IntegrityError:
        return False # Retorna False caso aconteça erro # Exemplo: atualizar para um email já existente
    finally:
        conexao_banco.close()  # Fecha a conexão com o banco


def excluir_dados(id_usuario):
    conexao_banco = sqlite3.connect("usuarios.db")
    cursor = conexao_banco.cursor() # Cria cursor para executar SQL

    comando_excluir = "DELETE FROM usuarios WHERE id = ?"

    try:
        cursor.execute(comando_excluir, (id_usuario,))
        if cursor.rowcount == 0:
            return None
        conexao_banco.commit() # Salva as alterações realizadas
        return True # Retorna True indicando que a atualização foi executada
    except sqlite3.OperationalError:
        return False # Retorna False caso aconteça erro # Exemplo: atualizar para um email já existente
    finally:
        conexao_banco.close() # Fecha a conexão com o banco




