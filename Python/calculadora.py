#Calculadora python 24/07/2023
print("bem vindo a Calculadora!!")

n1 = int(input("Digite um numero: "))

print("(+) Soma, (-) Subtração, (*) Multiplicação, (/) Divisão")
operador = input("Qual Operação você deseja realizar? ")

n2 = int(input("Digite outro numero: "))

if(operador == "+"):
    resultado = n1 + n2
    print("O resultado da operação foi: {}".format(resultado))
    
elif(operador == "-"):
    resultado = n1 - n2
    print("O resultado da operação foi: {}".format(resultado))
    
elif(operador == "*"):
    resultado = n1 * n2
    print("O resultado da operação foi: {}".format(resultado))

elif(operador == "/"):
    resultado = n1 / n2
    print("O resultado da operação foi: {}".format(resultado))

else:
    print("Operador invalido!")