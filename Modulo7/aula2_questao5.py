import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    
    return ' '.join(palavras_embaralhadas)

# Entrada do usuário
frase = input("Digite uma frase: ")
print(embaralhar_palavras(frase))