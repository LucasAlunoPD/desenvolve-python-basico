
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


soma = numero1 + numero2


if soma % 2 == 0:
    print(f"A soma dos dois números ({soma}) é PAR.")
else:
    print(f"A soma dos dois números ({soma}) é ÍMPAR.")
