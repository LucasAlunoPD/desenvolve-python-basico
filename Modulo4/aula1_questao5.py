
n = int(input("Digite a quantidade de respondentes: "))


if n <= 0:
    print("O número de respondentes deve ser maior que zero.")
else:
    soma_idades = 0 

    for i in range(n):
        idade = int(input(f"Digite a idade do respondente {i + 1}: "))
        soma_idades += idade  

   
    media = soma_idades / n


    print(f"A média de idade dos respondentes é: {media:.2f}")
