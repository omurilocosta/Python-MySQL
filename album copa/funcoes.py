import mysql.connector
from random import randint

def conectarBancoDados():
    try:
        conexao = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Msc9949027",
                                    database="album")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        return conexao

def mostrarMenu():
    print()
    print("#####################")
    print("### ÁLBUM DA COPA ###")
    print("#####################")
    print("Selecione a opção desejada:")
    print("1 - Ver Álbum Completo")
    print("2 - Ver um time")
    print("3 - Checar se tem uma figurinha")
    print("4 - Abrir um pacote de figurinhas")
    print("5 - Reiniciar álbum.")
    print("0 - Sair")
    print()
    resposta = int(input("Número da sua opção: "))
    print()
    return resposta

def verAlbum(parCursor, parPais):
    sql = "SELECT * FROM figurinhas,paises WHERE figurinhas.id_pais = paises.id"
    if parPais != 0:
        sql += f" AND paises.id = '{parPais}'"        

    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    
    for linha in tabelaSelect:
        tem = "[X]" if linha[4] else "[ ]"
        print(f"{tem} {linha[6]} - {linha[1]}{linha[3]} - {linha[2]}")

def escolherPais(parCursor):
    sql = "SELECT * FROM paises"
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    print("Códigos dos países:\n")
    for linha in tabelaSelect:
        print(f"{linha[0]} - {linha[1]}")
    codigoPais = input("Informe o código do país desejado: ")
    print()
    verAlbum(parCursor, codigoPais)

def checarFigurinha(parCursor):
    figurinha = input("Informe o código da figurinha: ")
    idPais = figurinha[:3]
    numero = int(figurinha[3:])
    sql = f"SELECT * FROM figurinhas, paises WHERE id_pais = '{idPais}' AND numero = {numero} AND figurinhas.id_pais = paises.id"    
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    if len(tabelaSelect) == 0:
        print("Código inválido.")
    else:
        linha = list(tabelaSelect[0])
        tem = "tem" if linha[4] else "não tem"
        print(f"{linha[6]} - {linha[1]}{linha[3]} - {linha[2]}")
        print(f"Você {tem} essa figurinha.")
        print()

def abrirPacote(parCursor):
    codigosPaises = []
    sql = "SELECT id FROM paises "    
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    for linha in tabelaSelect:
        codigosPaises.append(linha[0])

    for i in range(5):
        pais = codigosPaises[randint(0,len(codigosPaises)-1)]
        numero = randint(1,20)
        sql = f"SELECT jogador, tem FROM figurinhas WHERE id_pais = '{pais}' AND numero = {numero}"
        parCursor.execute(sql)
        tabelaSelect = parCursor.fetchall()
        for linha in tabelaSelect:
            jogador = linha[0]
            tem = "[repetida]" if linha[1] else ""
        figurinha = f"{pais}{numero}"
        print(f"Você tirou a figurinha {figurinha}: {tem} {jogador}")
        sql = f"UPDATE figurinhas SET tem = 1 WHERE id_pais = '{pais}' AND numero = {numero}"
        parCursor.execute(sql)

def limparAlbum(parCursor):
    resposta = input("Tem certeza que deseja deletar todas as figurinhas do álbum? sim|não ")
    if resposta == "sim":
        sql = "UPDATE figurinhas SET tem = 0"
        parCursor.execute(sql)
        print("Álbum reiniciado.")
    else:
        print("Entendido.")