class ListaDeCompras:
    itens = []
    quantidades = []

    def adicionar_item(self, nome_do_produto, quantidade):
        self.itens.append(nome_do_produto)
        self.quantidades.append(quantidade)

    def remover_item(self, indice):
        self.itens.pop(indice)
        self.quantidades.pop(indice)

    def listar_itens(self):
        i = 0
        while (i < len(self.itens)):
            print(str(self.quantidades[i]) + ' ' + self.itens[i])
            i = i+1


lista = ListaDeCompras()
lista.adicionar_item('Banana', 12)
lista.adicionar_item('Maçã', 58)
lista.adicionar_item('Melão', 16)
lista.adicionar_item('Abacaxi', 27)
lista.adicionar_item('Uva', 69)
lista.remover_item(2) # Remove Melão
lista.listar_itens()