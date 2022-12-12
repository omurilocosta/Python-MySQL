#Nomes: Allan Santos, Bruna Fontana e Murilo Costa
#Turma: 2° Info B

import mysql.connector 
from func import *

conexao = conectarBancoDados()
cursor = conexao.cursor()

while True:
    opcao = mostrarMenu()

    if opcao == 1:
        verEstacionamento(cursor,0)
    elif opcao == 2:
        escolherPavimento(cursor)
    elif opcao == 3:
        checarVaga(cursor)
    elif opcao == 4:
        alterarVaga(cursor,0)
        conexao.commit()
    elif opcao == 5:
        limparEstacionamento(cursor)
        conexao.commit()
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")

    input("Pressione ENTER para retornar ao menu.")