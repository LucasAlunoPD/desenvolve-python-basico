def validar_cpf(cpf):
    
    cpf = ''.join(filter(str.isdigit, cpf))


    if len(cpf) != 11:
        return False

    
    def calcular_digito(cpf, peso_inicial):
        soma = sum(int(cpf[i]) * (peso_inicial - i) for i in range(len(cpf)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    
    primeiro_digito = calcular_digito(cpf[:9], 10)


    segundo_digito = calcular_digito(cpf[:9] + str(primeiro_digito), 11)

   
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


cpf = input("Digite o CPF somente numeros: ")


if validar_cpf(cpf):
    print("Válido")
else:
    print("Inválido")