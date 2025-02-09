import string

def eh_palindromo(frase):

    frase_limpa = ''.join([char.lower() for char in frase if char not in string.punctuation and char != ' '])

    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')