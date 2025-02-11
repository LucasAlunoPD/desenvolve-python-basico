import csv
from collections import defaultdict


nome_arquivo = "spotify-2023.csv"


top_musicas = {}


with open(nome_arquivo, "r", encoding="latin-1") as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)  
    
    for linha in leitor_csv:
        try:
            track_name = linha[0]
            artist_name = linha[1]
            artist_count = int(linha[2])
            released_year = int(linha[3])
            streams = int(linha[8])
            
            if 2014 <= released_year <= 2025:
              
                if released_year not in top_musicas or streams > top_musicas[released_year][3]:
                    top_musicas[released_year] = [track_name, artist_name, released_year, streams]
        except (ValueError, IndexError):
        
            continue


lista_top_musicas = [top_musicas[ano] for ano in sorted(top_musicas.keys())]


print(lista_top_musicas)