
import random

def main():  

    numero_aleatorio = random.randint(1, 10)

    print("Adivinhe o número entre 1 e 10: ")

    while True:
        
        palpite = int(input("Digite o numero: "))

       
        if palpite < numero_aleatorio:
            print("Muito baixo. Tente novamente.")
        elif palpite > numero_aleatorio:
            print("Muito alto. Tente novamente.")
        else:
            print("Você acertou o número.")
            break


main()