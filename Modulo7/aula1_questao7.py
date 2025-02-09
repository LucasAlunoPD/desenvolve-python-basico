import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    print(f"Chave de criptografia: {chave_aleatoria}")

    nomes_cript = []

    for nome in nomes:
        nome_cript = ""
        for c in nome:
            novo_c = ord(c) + chave_aleatoria
            if novo_c > 126:
                novo_c -= 94
            nome_cript += chr(novo_c)
        nomes_cript.append(nome_cript)

    return nomes_cript

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript = encrypt(nomes)
print(f"Nomes criptografados: {nomes_cript}")