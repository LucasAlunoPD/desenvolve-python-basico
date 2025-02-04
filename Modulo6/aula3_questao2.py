def extrair_dominios(urls):
    return [url[4:-4] for url in urls]

def main():
    urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
    dominios = extrair_dominios(urls)
    print("Domínios:", dominios)

if __name__ == "__main__":
    main()