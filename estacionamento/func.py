import mysql.connector
from random import randint

def conectarBancoDados():
    try:
        conexao = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="ifcbrusque",
                                    database="estacionamento")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        return conexao

def mostrarMenu():
    print()
    print("######################")
    print("### Estacionamento ###")
    print("######################")
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
    vaga = input("Informe o código da vaga. Sendo o 1° digito o Andar(1,2,3) e o 2° digito a vaga(1-10)\nDigite o código:  ")
    idPavimeto = vaga[:1]
    numero = int(vaga[1:])
    sql = f"SELECT * FROM vagas, pavimentos WHERE vagas.id_pavimento = '{idPavimeto}' AND vagas.numero = {numero} AND vagas.id_pavimento = pavimentos.id"    
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    if len(tabelaSelect) == 0:
        print("Código inválido.")
    else:
        linha = list(tabelaSelect[0])
        LUGAR = "Ocupada" if linha[3] else "Vazia"
        print(f" Vaga n° {linha[2]} do {linha[5]}  ➜  {LUGAR}")
        print()

def alterarVaga(parCursor,parPavimento):
    codigosPavimentos = [] 
    sql = "SELECT id from vagas WHERE ocupada = '0'"
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    for linha in tabelaSelect:
        codigosPavimentos.append(linha[0])
    
    andar = int(input("Em qual andar vc deseja estacionar:\n1. Terreo\n2. G1\n3. G2\nNúmero da sua opção: "))
    numero = int(input("Em qual vaga vc deseja estacionar:1-10  "))
    while True:
        sql = f"SELECT * FROM vagas, pavimentos WHERE vagas.id_pavimento = {andar} AND vagas.numero = {numero}"
        if parPavimento != 0:
            sql += f" AND pavimentos.id = '{parPavimento}'"
        
        parCursor.execute(sql)
        tabelaSelect1 = parCursor.fetchall()
        for linha in tabelaSelect1:
            id_vaga = linha[0]
            LUGAR = "Ocupada" if linha[3] else "Vazia"
        
        if id_vaga in codigosPavimentos:
            print(f" Vaga n° {linha[2]} do {linha[5]} ➜  {LUGAR}")
            print("Automóvel estacionado")
            print()
            break
        else:
            print(f" Vaga n° {linha[2]} do {linha[5]} ➜  {LUGAR}")
            print("Tente outra vaga")
            print()
            andar = int(input("Em qual andar vc deseja estacionar:\n1. Terreo\n2. G1\n3. G2\nNúmero da sua opção: "))
            numero = int(input("Em qual vaga vc deseja estacionar:1-10  "))

    sql = f"UPDATE vagas SET ocupada = '1' WHERE vagas.id_pavimento = {andar} AND vagas.numero = {numero}"
    parCursor.execute(sql)

def limparEstacionamento(parCursor):
    resposta = input("Tem certeza que deseja esvaziar todas as vagas do estacionamento? sim|não\n ")
    if resposta == "sim":
        sql = "UPDATE vagas SET ocupada = 0"
        parCursor.execute(sql)
        print("Estacionamento reiniciado.")
    else:
        print("Entendido.")