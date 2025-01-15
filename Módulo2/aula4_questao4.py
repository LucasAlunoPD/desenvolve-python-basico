
valor = int(input())


notas = [100, 50, 20, 10, 5, 2, 1]


for nota in notas:
    qtd_notas = valor // nota  
    valor = valor % nota  
    print(f"{qtd_notas} nota(s) de R${nota},00")
