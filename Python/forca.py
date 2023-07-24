import random

def jogar():
    
    bem_vindo()

    palavra_secreta = palavras_secretas()
    
        
    letras_acertadas = ["_" for letra in palavra_secreta]
    chances = len(letras_acertadas) + 2
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
            print(erros)
        enforcou = erros == chances
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

def bem_vindo():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')
    
def palavras_secretas():
    palavras = []
    with open("palavras.txt", "r", encoding=("UTF-8")) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
    



if(__name__ == '__main__'):
    jogar()

    #gabriel