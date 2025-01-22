# Solicita as informações ao usuário
idade = int(input("Digite sua idade: "))
ja_jogou = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "True"
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica se o usuário atende aos critérios
apto = 16 <= idade <= 18 and ja_jogou and vitorias >= 1

# Imprime o resultado
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)

