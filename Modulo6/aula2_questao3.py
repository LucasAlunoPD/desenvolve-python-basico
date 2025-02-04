import random
from collections import Counter

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma = sum(elementos)
media = soma / num_elementos

print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", media)

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(set(lista1) & set(lista2))

print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("Interseccao ordenada:", interseccao)

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

for elemento in interseccao:
    print(f"Elemento {elemento} aparece {contagem_lista1[elemento]} vez(es) na Lista 1 e {contagem_lista2[elemento]} vez(es) na Lista 2")