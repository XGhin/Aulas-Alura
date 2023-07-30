import random

def jogar():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")
    
    palavras = []
    with open("palavras.txt", "r", encoding="UTF-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip().upper()
            palavras.append(linha)
    
    #sorteio de palavra
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero]
    
            
    #Letras acertadas
    letras_acertadas = []
    for letra in palavra_secreta:
        letra = letras_acertadas.append("_")
    
    enforcou = False
    ganhou = False
    erros = 0
    
    print(letras_acertadas)
    while (not enforcou and not ganhou):
        chute = input("Qual o seu chute? ").strip().upper()
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute.upper == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1    

if(__name__ == "__main__"):
    jogar()