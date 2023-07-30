class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("O extrato da conta {} (Titular: {}) é R${}".format(self.numero, self.titular, self.saldo))
        
    def sacar(self, valor):
        self.saldo -= valor
        print("O saldo atualizado da conta de {} é de R${}".format(self.titular, self.saldo))
        
    def depositar(self, valor):
        self.saldo += valor
        print("O saldo atualizado da conta de {} é de R${}".format(self.titular, self.saldo))
    
    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)
        