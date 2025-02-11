
def contar_mencoes(texto, palavra):
    
    return texto.lower().split().count(palavra.lower())


with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()


print("=== Primeiras 25 linhas ===")
for linha in linhas[:25]:
    print(linha.strip())  


num_linhas = len(linhas)
print(f"O arquivo possui {num_linhas} linhas.\n")

linha_mais_longa = max(linhas, key=len)
print(f"A linha com mais caracteres é:\n{linha_mais_longa.strip()}")
print(f"Tamanho: {len(linha_mais_longa)} caracteres\n")


texto_completo = " ".join(linhas) 
mencoes_nonato = contar_mencoes(texto_completo, "Nonato")
mencoes_iria = contar_mencoes(texto_completo, "Íria")

print(f"Número de menções a 'Nonato': {mencoes_nonato}")
print(f"Número de menções a 'Íria': {mencoes_iria}")