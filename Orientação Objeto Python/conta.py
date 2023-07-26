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
        print("O saldo atualizado da conta é de R${}".format(self.saldo))
        
    def depositar(self, valor):
        self.saldo += valor
        print("O saldo atualizado da conta é de R${}".format(self.saldo))    
        