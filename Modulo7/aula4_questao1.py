import os

frase = input("Digite uma frase: ")


nome_arquivo = "frase.txt"

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_completo = os.path.join(diretorio_atual, nome_arquivo)


with open(caminho_completo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

print(f"Arquivo salvo em: {caminho_completo}")
