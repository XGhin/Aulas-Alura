class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O extrato da conta {} (Titular: {}) é R${}".format(self.__numero, self.__titular, self.__saldo))

    def sacar(self, valor):
        self.__saldo -= valor
        print("O saldo atualizado da conta de {} é de R${}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor
        print("O saldo atualizado da conta de {} é de R${}".format(self.__titular, self.__saldo))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

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
