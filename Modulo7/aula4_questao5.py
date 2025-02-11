import csv


nome_arquivo = "meus_livros.csv"


livros = [
    ["Título", "Autor", "Ano de publicação", "Número de páginas"],
    ["O Sol é Para Todos", "Harper Lee", 1960, 336],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["Neuromancer", "William Gibson", 1984, 271],
    ["Crime e Castigo", "Fiódor Dostoiévski", 1866, 671],
    ["Fundação", "Isaac Asimov", 1951, 255],
    ["Duna", "Frank Herbert", 1965, 896],
    ["A Guerra dos Tronos", "George R.R. Martin", 1996, 694],
    ["O Nome do Vento", "Patrick Rothfuss", 2007, 662],
    ["O Código Da Vinci", "Dan Brown", 2003, 689],
    ["Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005, 400]
]


with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(livros)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
