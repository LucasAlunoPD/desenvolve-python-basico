
classe = input("Qual seu genero H ou M :")         

idade=int(input('Qual sua idade ?'))
tempo= int(input('Quantos anos voce trabalhou na vida: '))

if classe == "H":
    aposentado= idade >= 65 or tempo >=30

elif classe =="M":
    aposentado= idade >= 60 or tempo >= 25

else:
    aposentado= False


print("Voce é aposentado:",aposentado )



