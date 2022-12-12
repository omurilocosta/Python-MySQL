import mysql.connector
from random import randint

def conectarBancoDados():
    try:
        conexao = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Msc9949027",
                                    database="estacionamento")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        return conexao

def mostrarMenu():
    print()
    print("#####################")
    print("### Estacionamento ###")
    print("#####################")
    print("Selecione a opção desejada:")
    print("1 - Ver estacionamento")
    print("2 - Escolher pavimento")
    print("3 - Checar vaga")
    print("4 - Alterar vaga")
    print("5 - Esvaziar Estacionamento.")
    print("0 - Sair")
    print()
    resposta = int(input("Número da sua opção: "))
    print()
    return resposta

def verEstacionamento(parCursor, parPavimento):
    sql = "SELECT * FROM vagas,pavimentos WHERE vagas.id_pavimento = pavimentos.id"
    if parPavimento != 0:
        sql += f" AND pavimentos.id = '{parPavimento}'"        

    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    
    for linha in tabelaSelect:
        LUGAR = "Ocupada" if linha[3] else "Vazia"
        print(f" {linha[5]} vaga n° {linha[2]}  ➜  {LUGAR}")

def escolherPavimento(parCursor):
    sql = "SELECT * FROM pavimentos"
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    print("Códigos dos pavimentos:\n")
    for linha in tabelaSelect:
        print(f"{linha[0]} - {linha[1]}")
    codigoPavimento = input("Informe o código do pavimento desejado: ")
    print()
    verEstacionamento(parCursor, codigoPavimento)

def checarVaga(parCursor):
    vaga = input("Informe o código da vaga: ")
    idPavimeto = vaga[:3]
    numero = int(vaga[2:])
    sql = f"SELECT * FROM vagas, pavimetos WHERE id_pavimento = '{idPavimeto}' AND numero = {numero} AND vagas.id_pavimento = pavimentos.id"    
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    if len(tabelaSelect) == 0:
        print("Código inválido.")
    else:
        linha = list(tabelaSelect[0])
        tem = "tem" if linha[3] else "não tem"
        print(f"{linha[5]} - {linha[1]}{linha[3]} - {linha[2]}")
        print(f"Você {tem} essa figurinha.")
        print()

def alterarVaga(parCursor):
    codigosPavimentos = [] 
    sql = "SELECT id from vagas WHERE ocupada = '0'"
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    for linha in tabelaSelect:
        codigosPavimentos.append(linha[0])
        
    numero = int(input("Em qual vaga vc deseja estacionar:  "))
    while True:
        if numero in codigosPavimentos:
            print(f"Vaga {numero} está vazia")
            print()
            break
        else:
            print(f"Vaga {numero} está ocupada. Tente outra")
            print()
            numero = int(input("Em qual vaga vc deseja estacionar:  "))

    sql = f"UPDATE vagas SET ocupada = 1 WHERE numero = {numero}"
    parCursor.execute(sql)

def limparEstacionamento(parCursor):
    resposta = input("Tem certeza que deseja esvaziar todas as vagas do estacionamento? sim|não ")
    if resposta == "sim":
        sql = "UPDATE vagas SET ocupada = 0"
        parCursor.execute(sql)
        print("Estacionamento reiniciado.")
    else:
        print("Entendido.")