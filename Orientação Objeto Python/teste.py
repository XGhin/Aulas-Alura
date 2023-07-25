def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def sacar(conta, valor):
    conta["saldo"] -= valor

def depositar(conta, valor):
    conta["saldo"] += valor

def extrato(conta):
    print("seu saldo é {}".format(conta["saldo"]))
