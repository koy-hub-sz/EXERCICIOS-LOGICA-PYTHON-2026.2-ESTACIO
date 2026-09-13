print("CADASTRO DE CIDADES BRASILEIRAS")

cidades = []

for i in range(1, 6):

    print(f"\nCadastro da cidade {i}")

    while True:
        nome = input("Nome da cidade: ").strip()

        if nome:
            break
        else:
            print("Erro: o nome da cidade não pode ficar vazio.")

    while True:
        estado = input("Estado (sigla com 2 letras): ").strip().upper()

        if len(estado) == 2 and estado.isalpha():
            break
        else:
            print("Erro: informe uma sigla válida com 2 letras.")

    while True:
        try:
            populacao = int(input("População estimada: "))

            if populacao >= 0:
                break
            else:
                print("Erro: a população não pode ser negativa.")

        except ValueError:
            print("Erro: digite a população usando números inteiros.")

    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

    cidades.append(cidade)

maior_populacao = cidades[0]

menor_populacao = cidades[0]

populacao_total = 0

for cidade in cidades:

    populacao_total += cidade["populacao"]

    if cidade["populacao"] > maior_populacao["populacao"]:
        maior_populacao = cidade

    if cidade["populacao"] < menor_populacao["populacao"]:
        menor_populacao = cidade

media_populacional = populacao_total / len(cidades)

print("\n")
print("CIDADES CADASTRADAS")

for cidade in cidades:
    print(f"Cidade:     {cidade['nome']}")
    print(f"Estado:     {cidade['estado']}")
    print(f"População:  {cidade['populacao']:,}".replace(",", "."))
    print("-" * 55)

print("ANÁLISE POPULACIONAL")

print(
    f"Maior população: "
    f"{maior_populacao['nome']} - "
    f"{maior_populacao['populacao']:,}".replace(",", ".")
)

print(
    f"Menor população: "
    f"{menor_populacao['nome']} - "
    f"{menor_populacao['populacao']:,}".replace(",", ".")
)

print(
    f"População total:  "
    f"{populacao_total:,}".replace(",", ".")
)

print(f"Média populacional: {media_populacional:.2f}")