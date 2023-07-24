print("****************************")
print("Bem vindo ao jogo da Forca!!")
print("****************************")

palavras = []
with open("palavras.txt", "r", encoding=("UTF-8")) as arquivo:
    for linha in arquivo:
        linha = linha.strip
        palavras.append(linha)
        