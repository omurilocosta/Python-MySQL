import classesGame
import random
import introducao 
# ESSE ARQUIVO É APENAS UM EXEMPLO DE COMO USAR AS CLASSES
# SEU CONTEÚDO DEVE SER APAGADO PARA SEGUIR O ROTEIRO DA AVALIAÇÃO 
# AS INSTRUÇÕES ESTÃO POSTADAS NO SIGAA
#  

print("Bem-vindo à Melchior")
input()
print("Para iniciar sua aventura, precisamos criar seu personagem: ")
nome = input("Escolha vosso nome de guerreiro: ")
categoria = input("Diga nos vossa categoria: ")
jogador = classesGame.Player(nome, categoria)
nome = jogador.obterNome()



print("(TELA DE CARREGAMENTO LEGAL...)")
input()

intro = introducao.historia(nome)
print(intro)

print("(TELA DE CARREGAMENTO LEGAL...)")
input()

print("...: Olá meu querido aventureiro, me chamo Bentley.")
print("Bentley: Imagino o porque você veio até mim. Vou ajudar-lhe em sua jornada")
print("Bentley: Tome... pegue esses itens aqui.")
print(f"{nome}: O-obrigado...")

item = classesGame.Item("Peitoral","Proteção para seus peitos",75,1)
jogador.inventario.adicionarItem(item)

item2 = classesGame.Item("Mingau","Comida que aumenta a vida",5,1)
jogador.inventario.adicionarItem(item2)

item3 = classesGame.Item("Espada","Curta e afiada",50,1)
jogador.inventario.adicionarItem(item3)

item4 = classesGame.Item("Escudo","Duro e grosso",30,1)
jogador.inventario.adicionarItem(item4)

item5 = classesGame.Item("Adaga","Arma branca",35,1)
jogador.inventario.adicionarItem(item5)

print('É hora de iniciar sua aventura em direção a Melchior')
print('Após caminhar por mais de meia hora, algo começa a se mecher no meio da floresta. Curioso, você decide chegar mais perto...')
print('JULIETTE DO BBB | 80 DE VIDA')
print(f'{nome}: Mas o que?')


print("Primeira batalha")

vida_player = jogador.obterVida()
jogador.alterarVida(vida_player)
vida_juju =80

while vida_juju > 0: 
    
    dano_juju = random.randint(1,20)
    vida_player -= dano_juju
    if vida_player < 0:
        vida_player = 0 
    print("\nVez de Juliette")
    input()
    print("Juliette lançou um cuscuz em você e lhe deu", dano_juju, "de dano")
    print("Sua vida atual:",vida_player)
    if vida_player > 0:
        dano_player = random.randint(1,20)
        vida_juju -= dano_player
        if vida_juju < 0:
            vida_juju = 0
        print("\nSua vez")
        input()
        print("Você tacou farinha nela e deu ", dano_player," de dano")
        print("Vida atual Juju:", vida_juju)
    elif vida_player <= 0:
        vida_player = 0
        print()
        COMIDA = input("Informe se você tem comida: sim|nao \n")
        if COMIDA == "sim":
            jogador.inventario.descartarItem()
            comer = random.randint(1,20)
            vida_player += comer
            print()
            print(f"Você recebeu {comer} de vida")
            print("Sua nova vida é:", vida_player)
        else:
            print("Você lutou bravamente, mas seu oponente se mostrou superior na batalha e venceu-a!")
            break

if vida_player > 0:        
    print("\nParabéns! Você derrotou seu primeiro oponente")
    print("Receba aqui uma premiação por sua vitória...")
    print("Um pernil de porco bem suculento e um diamante muito valioso.")
    print("Um diamante raro que será importante na sua aventura.")
    print()
    item1_batalha1 = classesGame.Item("Pernil de porco", "Uma carne bem suculenta e macia que regenera parte de sua vida", 10, 1)
    item2_batalha1 = classesGame.Item("Diamante", "Pedra preciosa grande valor", 1000, 1)
    jogador.inventario.adicionarItem(item1_batalha1)
    jogador.inventario.adicionarItem(item2_batalha1)
    