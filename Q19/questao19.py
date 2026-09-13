print("ANÁLISE LINGUÍSTICA DE UMA FRASE")

while True:
    frase = input("Digite uma frase: ").strip()

    if frase:
        break
    else:
        print("Erro: a frase não pode estar vazia.")

frase_formatada = " ".join(frase.split())

palavras = frase_formatada.split()

while True:
    letra = input("Digite uma letra para pesquisar: ").strip()

    if len(letra) == 1 and letra.isalpha():
        break
    else:
        print("Erro: digite apenas uma letra.")

quantidade_letra = frase_formatada.lower().count(letra.lower())

quantidade_caracteres = len(frase_formatada)
quantidade_palavras = len(palavras)
primeira_palavra = palavras[0]
ultima_palavra = palavras[-1]

print("\n")
print("RELATÓRIO")

print(f"Frase:                 {frase_formatada}")
print(f"Quantidade de caracteres: {quantidade_caracteres}")
print(f"Quantidade de palavras:   {quantidade_palavras}")
print(f"Primeira palavra:         {primeira_palavra}")
print(f"Última palavra:           {ultima_palavra}")
print(
    f"Ocorrências da letra "
    f"'{letra}': {quantidade_letra}"
)
print(f"Frase em maiúsculas:      {frase_formatada.upper()}")
print(f"Frase em minúsculas:      {frase_formatada.lower()}")