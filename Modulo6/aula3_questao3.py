import random

def gerar_lista():
    return [random.randint(-10, 10) for _ in range(20)]

def encontrar_intervalo_negativos(lista):
    max_intervalo = (0, 0)
    inicio = None

    for i, num in enumerate(lista):
        if num < 0:
            if inicio is None:
                inicio = i
        else:
            if inicio is not None:
                if (i - inicio) > (max_intervalo[1] - max_intervalo[0]):
                    max_intervalo = (inicio, i)
                inicio = None

    if inicio is not None and (len(lista) - inicio) > (max_intervalo[1] - max_intervalo[0]):
        max_intervalo = (inicio, len(lista))

    return max_intervalo

def main():
    lista = gerar_lista()
    print("Lista original:", lista)

    inicio, fim = encontrar_intervalo_negativos(lista)
    if inicio != fim:
        del lista[inicio:fim]

    print("Lista após remoção do intervalo de negativos:", lista)

if __name__ == "__main__":
    main()
