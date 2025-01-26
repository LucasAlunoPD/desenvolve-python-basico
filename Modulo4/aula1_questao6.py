# Leia o número de experimentos
n = int(input())

# Inicialização das variáveis
total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

# Processar cada experimento
for _ in range(n):
    # Leia a quantidade e o tipo de cobaia
    entrada = input().split()
    quantidade = int(entrada[0])
    tipo = entrada[1]

    # Atualize o total de cobaias e de cada tipo
    total_cobaias += quantidade
    if tipo == 'C':  # Coelho
        total_coelhos += quantidade
    elif tipo == 'R':  # Rato
        total_ratos += quantidade
    elif tipo == 'S':  # Sapo
        total_sapos += quantidade

# Calcular os percentuais
percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0

# Exibir os resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")

