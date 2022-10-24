import mysql.connector
import funcao

host_ = input("Digite o host do banco:  \n")
user_ = input("Digite qual é o seu usuário:  \n")
password_ = input("Digite a senha do banco:  \n")

list_ = []

try:
    conexao = mysql.connector.connect(
        host = host_,
        user = user_,
        password = password_
    )

    cursor = conexao.cursor()

    database_ = input("Qual vai ser o nome do banco? \n")

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_}")
    conexao.commit()
    print("DATABASE criada com sucesso!")

    conexao.database = database_

    table_ = input("Informe o nome da tabela:  \n")
    campos = int(input("Quantos campos sua tabela vai ter?  \n"))
    aviso = print("AVISO: O primeiro campo deve ser obrigatoriamente o ID!!")
    numb = 1

    id = input("Informe o ID da tabela:  ")
    feijao = (f"{id} int auto_increment,")
    list_.append(feijao)

    while numb != campos:
        nome = input('Qual vai ser o nome desse campo:  \n')
        arroz = (f"{nome} VARCHAR(30),")
        list_.append(arroz)
        numb += 1

    funcao.CREATE(list_, table_, id, cursor)
    conexao.commit()

except Exception as erro:
    print(f"Erro: {erro}")
