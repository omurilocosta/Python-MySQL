class Player:
    # nome
    # categoria
    # inventário
    # vida
    # dinheiro
    pass

class Item:
    def __init__(self, parNome, parDescricao, parValor, parQuantidade):    
        self.__nome = parNome
        self.__descricao = parDescricao
        self.__valor = parValor
        self.__quantidade = parQuantidade

    # nome
    def ObterNome(self):
        return self.__nome

    def AlterarNome(self, parNome):
        self.__nome = parNome

    # descricao
    def ObterDescricao(self):
        return self.__descricao

    def AlterarDescricao(self, parDescricao):
        self.__descricao = parDescricao

    #valor
    def ObterValor(self):
        return self.__valor
    
    def AlterarValor(self, parValor):
        self.__valor = parValor

    # quantidade    
    def ObterQuantidade(self):
        return self.__quantidade

    def AlterarQuantidade(self, parQuantidade):
        self.__quantidade += parQuantidade

    # mostrar item
    def Mostrar(self):
        texto = f"Item: {self.__nome}\n"
        texto += f"Descrição: {self.__descricao}\n"
        texto += f"Valor: {self.__valor}\n"
        texto += f"Quantidade: {self.__quantidade}"
        return texto

class Inventory:
    # capacidade
    # itens
    # adicionar
    # vender
    # destacar
    # mostrar
    pass