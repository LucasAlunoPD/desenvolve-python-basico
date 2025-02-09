import string

def validador_senha(senha):

    if len(senha) < 8:
        return False


    if not any(c.isupper() for c in senha):
        return False

    if not any(c.islower() for c in senha):
        return False

    if not any(c.isdigit() for c in senha):
        return False


    caracteres_especiais = set(string.punctuation)
    if not any(c in caracteres_especiais for c in senha):
        return False


    return True


senha = input("Digite uma senha: ")


if validador_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")