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

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    def set_limite(self, limite):
        self.__limite = limite
