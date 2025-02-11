import random


def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]


def carregar_enforcado(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read().split("\n\n")

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_da_forca():
    palavras = carregar_palavras("gabarito_forca.txt")
    estagios = carregar_enforcado("gabarito_enforcado.txt")
    palavra = random.choice(palavras).upper()
    letras_descobertas = ["_" for _ in palavra]
    letras_tentadas = set()
    erros = 0
    
    print("Bem-vindo ao jogo da forca!")
    print(" ".join(letras_descobertas))
    
    while erros < 6 and "_" in letras_descobertas:
        letra = input("Digite uma letra: ").upper()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra!")
            continue
        
        letras_tentadas.add(letra)
        
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            erros += 1
            imprime_enforcado(erros, estagios)
        
        print(" ".join(letras_descobertas))
    
    if "_" not in letras_descobertas:
        print("Parabéns! Você acertou a palavra!", palavra)
    else:
        print("Game over! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()