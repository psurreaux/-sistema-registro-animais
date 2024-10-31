import sqlite3

import sqlite3

# Conectando-se ao banco de dados
conn = sqlite3.connect("animais.db")
cursor = conn.cursor()

# Criando a tabela 'animais'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sexo TEXT,
        idade INTEGER,
        qualidade TEXT
    )
''')

# Confirmando a criação e fechando a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela criados com sucesso!")
