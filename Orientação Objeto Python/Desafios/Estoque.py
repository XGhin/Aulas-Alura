class Estoque:
    itens = []

    def __init__(self, item, quantidade, valor):
        self._item = item
        self._quantidade = quantidade
        self._valor = valor
        Estoque.itens.append(item)

    def adicionar(self, quantidade):
        self._quantidade += quantidade

    def new_price(self, valor):
        self._valor = valor

    @property
    def estoque(self):
        return self._quantidade

    @property
    def valor(self):
        print("Item: {}\nValor: R${:.2f} Reais".format(self._item, self._valor))

