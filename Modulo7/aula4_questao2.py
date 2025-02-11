import os
import re

arquivo_origem = "frase.txt"
arquivo_destino = "palavras.txt"

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_origem = os.path.join(diretorio_atual, arquivo_origem)
caminho_destino = os.path.join(diretorio_atual, arquivo_destino)

with open(caminho_origem, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r"\b[a-zA-ZÀ-ÿ]+\b", conteudo)

with open(caminho_destino, "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

with open(caminho_destino, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
