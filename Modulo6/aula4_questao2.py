frase = input("Digite uma frase: ")

vogais = sorted([c for c in frase if c.lower() in "aeiou"])
consoantes = [c for c in frase if c.lower() in "bcdfghjklmnpqrstvwxyz"]

print("Vogais ordenadas:", vogais)
print("Consoantes sem espaços:", consoantes)
