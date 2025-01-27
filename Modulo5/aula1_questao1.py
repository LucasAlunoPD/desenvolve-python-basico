def main():
 
    numero1 = float(input("Digite o primeiro número decimal: "))
    numero2 = float(input("Digite o segundo número decimal: "))

  
    diferenca = abs(numero1 - numero2)

    
    diferenca_arredondada = round(diferenca, 2)

    
    print(f"A diferença entre os números é: {diferenca_arredondada}")


if __name__ == "__main__":
    main()