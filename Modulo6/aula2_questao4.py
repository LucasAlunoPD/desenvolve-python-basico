def obter_lista(mensagem):
    return list(map(int, input(mensagem).split()))

def intercalar_listas(lista1, lista2):
    resultado = []
    min_len = min(len(lista1), len(lista2))

    for i in range(min_len):
        resultado.append(lista1[i])
        resultado.append(lista2[i])

    resultado.extend(lista1[min_len:])
    resultado.extend(lista2[min_len:])

    return resultado

def main():
    lista1 = obter_lista("Digite os números da primeira lista, separados por espaço: ")
    lista2 = obter_lista("Digite os números da segunda lista, separados por espaço: ")

    lista_intercalada = intercalar_listas(lista1, lista2)
    print("Lista intercalada:", lista_intercalada)

if __name__ == "__main__":
    main()
