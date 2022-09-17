import random

class Player:

    def __init__(self, parNome, parCategoria):
        self.__nome = parNome
        self.__categoria = parCategoria
        self.__vida = 100
        self.__dinheiro = 1000
        # esse atributo ficará público e poderá ser acessado 
        # diretamente pelo programa principal: 
        self.inventario = Inventory(10)

    # nome
    def obterNome(self):
        return self.__nome

    def alterarNome(self, parNome):
        self.__nome = parNome

    # categoria
    def obterCategoria(self):
        return self.__categoria

    def alterarCategoria(self, parCategoria):
        self.__categoria = parCategoria

    # vida
    def obterVida(self):
        return self.__vida

    def alterarVida(self, parValor):
        if (self.__vida + parValor) < 0:
            self.__vida = 0
        elif (self.__vida + parValor) > 100:
            self.__vida = 100
        else:
            self.__vida += parValor

    # dinheiro
    def obterDinheiro(self):
        return self.__dinheiro

    def alterarDinheiro(self, parValor):
        if (parValor + self.__dinheiro) >= 0:
                self.__dinheiro += parValor
        else:
            print("Saldo insuficiente.")

class Item:
    def __init__(self, parNome, parDescricao, parValor, parQuantidade):
        self.__nome = parNome
        self.__descricao = parDescricao
        self.__valor = parValor
        self.__quantidade = parQuantidade

    # nome
    def obterNome(self):
        return self.__nome

    def alterarNome(self, parNome):
        self.__nome = parNome

    # descricao
    def obterDescricao(self):
        return self.__descricao

    def alterarDescricao(self, parDescricao):
        self.__descricao = parDescricao

    # valor
    def obterValor(self):
        return self.__valor

    def alterarValor(self, parValor):
        self.__valor = parValor

    # quantidade
    def obterQuantidade(self):
        return self.__quantidade

    def alterarQuantidade(self, parQuantidade):
        # self.__quantidade = self.__quantidade + parQuantidade
        if (parQuantidade + self.__quantidade) >= 0:
                self.__quantidade += parQuantidade
        else:
            print("Quantidade insuficiente.")
 
    # mostrar
    def mostrar(self):
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Valor: {self.__valor}")
        print(f"Quantidade: {self.__quantidade}")
 
class Inventory:
    def __init__(self, parCapacidade):
        self.__capacidade = parCapacidade
        self.__itens = []

    def obterItens(self):
        return self.__itens
    
    # capacidade
    def obterCapacidade(self):
        return self.__capacidade

    def alterarCapacidade(self, parCapacidade):
        self.__capacidade = parCapacidade

    # itens
    # adicionar
    def adicionarItem(self, parItem):
        quantidade = len(self.__itens)
        if self.__capacidade > quantidade:
            self.__itens.append(parItem)
        else:
            print("Inventário cheio. Impossível adicionar.")

    # mostrar
    def mostrarInventario(self):
        indice = 0
        for meuItem in self.__itens:
            print(f"\nItem {indice}:")
            meuItem.mostrar()
            indice +=1 

    # descartar
    def descartarItem(self):

        print("Para descartar um item, use o índice correspondente:\n")
        self.mostrarInventario()

        indiceRemover = int(input("Digite o número do item a remover:"))
        quantidade = len(self.__itens)
        if indiceRemover < quantidade:
            self.__itens.pop(indiceRemover)
        else: 
            print("Item inválido.")
