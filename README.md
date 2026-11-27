================================= Sistema de CRUD com Python e SQLite ====================================


O que é um CRUD?

CRUD é o acrônimo para as quatro operações fundamentais usadas em sistemas que lidam com bancos de dados:
• C - Create (Criar): Inserir novos registros no banco de dados (comando SQL: INSERT INTO).
• R - Read (Ler): Consultar e exibir dados já cadastrados (comando SQL: SELECT).
• U - Update (Atualizar): Modificar informações de um registro existente (comando SQL: UPDATE).
• D - Delete (Deletar): Remover um registro do banco de dados (comando SQL: DELETE FROM).


Explicação das funções: O código foi dividido em módulos para facilitar a manutenção e separar a lógica de negócios do acesso ao banco de dados:

├── conexao_banco.py   # Estabelece a conexão com o SQLite e cria a tabela inicial
├── repository.py      # Contém todas as funções SQL (Create, Read, Update, Delete)
├── main.py            # Interface principal (menu) e fluxo de execução do usuário
└── .gitignore         # Ignora arquivos locais temporários e o banco de dados (.db)

