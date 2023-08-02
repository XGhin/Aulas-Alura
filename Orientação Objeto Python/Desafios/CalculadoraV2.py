print("Bem vindo a Calculadora (2.0)")

print("(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n(^) Elevado")
operador = input("Qual operação você deseja fazer?")

def somar():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma foi: {}".format(n1+n2))

def subtrair():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("O resultado da subtração foi: {}".format(n1-n2))

def multiplicar():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("O resultado da multiplicação foi: {}".format(n1*n2))

def dividir():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("O resultado da divisão foi: {}".format(n1/n2))

def potencia():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("O resultado da potencia foi: {}".format(n1**n2))

if (operador == "+"):
    somar()
elif (operador == "-"):
    subtrair()
elif (operador == "*"):
    multiplicar()
elif (operador == "/"):
    dividir()
elif (operador == "^"):
    potencia()