import mysql.connector

def Tabela(parNomeTabela, parListaCampos):
    sql = f"CREATE TABLE {parNomeTabela} (id int AUTO_INCREMENT, "
    for campo in parListaCampos:
        sql = sql + f"{campo} VARCHAR(50),"

    sql = sql + "PRIMARY KEY(id) );"

listaCampos = []

servidor = input("Informe o endereço do servidor do banco de dados: \n")
usuario = input(f"\nInforme o usuário do servidor {servidor}: \n")
senha = input(f"\nInforme a senha do usuário {usuario}: \n")

try:
    conexao = mysql.connector.connect(
        host = servidor,
        user = usuario,
        password = senha
    )
    input("\nConectado com sucesso ao banco de dados. PRESSIONE ENTER.\n")
except Exception as erro:
    print(f"Erro de conexão: {erro}")

base = input("\nQual o nome da base que você vai criar? \n")

cursor = conexao.cursor()

try:
    if conexao.is_connected():
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {base}")
        print(f"\nBase {base} criada com sucesso.\n")
        conexao.database = base
    else:
        print("\nA conexão com banco de dados foi interrompida!\n")
except Exception as erro:
    print(f"Erro de conexão: {erro}")

nomeTabela = input("\nQual o nome da tabela que vocÊ deseja criar?\n")
qntsCampos = int(input(f"\nQuantos campos a tabela {nomeTabela} terá?\n"))

for campo in range(qntsCampos):
    nomeCampo = input(f"\nQual o nome do campo {campo+1}?\n")
    listaCampos.append(nomeCampo)

sql = Tabela(nomeTabela, listaCampos)

try:
    if conexao.is_connected():
        cursor.execute(sql)
        print(f"\nTabela {nomeTabela} criada com sucesso.\n")
    else:
        print("\nA conexão com o banco de dados foi interrompida.\n")
except Exception as erro:
    print(f"Erro: {erro}")
    