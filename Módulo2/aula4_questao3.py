

nome_produto1 = input("Digite o nome do primeiro produto: ")
preco_unitario1 = float(input(f"Digite o preço unitário de {nome_produto1}: "))
quantidade1 = int(input(f"Digite a quantidade de {nome_produto1}: "))

nome_produto2 = input("Digite o nome do segundo produto: ")
preco_unitario2 = float(input(f"Digite o preço unitário de {nome_produto2}: "))
quantidade2 = int(input(f"Digite a quantidade de {nome_produto2}: "))

nome_produto3 = input("Digite o nome do terceiro produto: ")
preco_unitario3 = float(input(f"Digite o preço unitário de {nome_produto3}: "))
quantidade3 = int(input(f"Digite a quantidade de {nome_produto3}: "))


total = (preco_unitario1 * quantidade1) + (preco_unitario2 * quantidade2) + (preco_unitario3 * quantidade3)


print(f"Total: R${total:,.2f}")