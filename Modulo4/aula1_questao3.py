n1=int(input('Digte a primeira nota: '))
n2=int(input('Digte a segunda nota: '))
n3=int(input('Digte a terceira nota: '))

m= (n1+n2+n3)/3

if m>= 60: 
    print('Aprovado')
elif m>=40: 
    print('Recuperação')
else:
    print('Reprovado')

print('fim')