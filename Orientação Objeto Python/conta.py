class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__saldo_disponivel = saldo + limite

    def extrato(self):
        print("O extrato da conta {} (Titular: {}) é R${}".format(self.__numero, self.__titular, self.__saldo))

    def sacar(self, valor):
        if (self.__saldo_disponivel >= valor):
            self.__saldo -= valor
            print("O saldo atualizado da conta de {} é de R${}".format(self.__titular, self.__saldo))
        else:
            print("saldo insuficiente para sacar R${}".format(valor))

    def depositar(self, valor):
        self.__saldo += valor
        print("O saldo atualizado da conta de {} é de R${}".format(self.__titular, self.__saldo))

    def transferir(self, valor, destino):
        if(valor <= self.__saldo_disponivel):
            self.sacar(valor)
            destino.depositar(valor)
        else:
            print("A conta de origem não possui credito suficiente!")    

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

