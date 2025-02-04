def obter_numeros():
    while True:
        numeros = list(map(int, input("Digite pelo menos 4 números inteiros, separados por espaço: ").split()))
        if len(numeros) >= 4:
            return numeros
        print("Você precisa digitar pelo menos 4 números.")

def exibir_resultados(lista):
    print("Lista original:", lista)
    print("3 primeiros elementos:", lista[:3])
    print("2 últimos elementos:", lista[-2:])
    print("Lista invertida:", lista[::-1])
    print("Elementos de índice par:", lista[::2])
    print("Elementos de índice ímpar:", lista[1::2])

def main():
    numeros = obter_numeros()
    exibir_resultados(numeros)

if __name__ == "__main__":
    main()

