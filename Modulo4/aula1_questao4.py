
n=int(input('Digite o valor: '))

maior = 0  

while n > 0:
    x = int(input('Digite um valor: '))

    if x > maior:  
        maior = x  
    n -= 1  


print("O maior valor é:", maior)


