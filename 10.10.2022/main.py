import mysql.connector 

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ifcbrusque"
        )
    print("Conectado com sucesso as servdor MySQL!")
except Exception as erro:
    print(f"Erro: {erro}")

cursor = conexao.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS 2INFOB")
    conexao.commit()
    print("DATABASE criada com sucesso!")
except Exception as erro:
    print(f"Erro ao executar as instruções SQL: {erro}")

conexao.database = "2infoB"

try:
    cursor.execute("""  CREATE TABLE IF NOT EXISTS cliente(
                                id VARCHAR(4), 
                                nome VARCHAR(80),
                                PRIMARY KEY(id)
                            );
                    """)
    cursor.execute("""  CREATE TABLE IF NOT EXISTS cliente_particular(
                                id VARCHAR(4),
                                cpf VARCHAR(34),
                                PRIMARY KEY(id),
                                FOREIGN KEY(id) REFERENCES cliente(id)
                            );
                    """)
    conexao.commit()
    print("TABELAS criadas com sucesso!")
except Exception as erro:
    print(f"Erro ao executar as instruções SQL: {erro}")

#fechar
cursor.close()
conexao.close()