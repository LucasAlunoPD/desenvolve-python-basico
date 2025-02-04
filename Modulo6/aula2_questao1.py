


import random
aleatorios= []
for i in range(20):

    valor=random.randint(-100,100)
    aleatorios.append(valor)

print(sorted(aleatorios))
print(aleatorios)
print("O maior valor é ", aleatorios.index(max(aleatorios)))
print("o menor valor", aleatorios.index(min(aleatorios)))