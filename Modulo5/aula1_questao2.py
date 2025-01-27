
n=int(input('Digite quantos numeros aleatorios deseja: '))

import random
import math


valores = [random.randint(0, 100) for _ in range(n)]


soma = sum(valores)


raiz_quadrada = math.sqrt(soma)


print(f"Valores gerados: {valores}")
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")