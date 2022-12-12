import mysql.connector 
from funcoes import *

conexao = conectarBancoDados()
cursor = conexao.cursor()

while True:
    opcao = mostrarMenu()

    if opcao == 1:
        verAlbum(cursor,0)
    elif opcao == 2:
        escolherPais(cursor)
    elif opcao == 3:
        checarFigurinha(cursor)
    elif opcao == 4:
        abrirPacote(cursor)
        conexao.commit()
    elif opcao == 5:
        limparAlbum(cursor)
        conexao.commit()
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")

    input("Pressione ENTER para retornar ao menu.")
