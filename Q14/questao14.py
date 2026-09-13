def ler_nota(numero_nota):
    
    while True:
        try:
            nota = float(
                input(f"Digite a {numero_nota}ª nota (0 a 10): ")
                .replace(",", ".")
            )

            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("Erro: digite uma nota válida.")


def calcular_media(nota1, nota2, nota3):
    
    return (nota1 + nota2 + nota3) / 3

print("SISTEMA DE NOTAS DA TURMA")

estudantes = []

for i in range(1, 6):

    print(f"\n Cadastro do estudante {i}")

    nome = input("Nome do estudante: ").strip()

    nota1 = ler_nota(1)
    nota2 = ler_nota(2)
    nota3 = ler_nota(3)

    media = calcular_media(nota1, nota2, nota3)

    estudante = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    estudantes.append(estudante)

maior_media = estudantes[0]
menor_media = estudantes[0]

aprovados = 0
recuperacao = 0
reprovados = 0

for estudante in estudantes:

    if estudante["media"] > maior_media["media"]:
        maior_media = estudante

    if estudante["media"] < menor_media["media"]:
        menor_media = estudante

    if estudante["media"] >= 7:
        aprovados += 1

    elif estudante["media"] >= 5:
        recuperacao += 1

    else:
        reprovados += 1

print("\n")
print("MÉDIA DOS ESTUDANTES")

for estudante in estudantes:
    print(
        f"{estudante['nome']:<25} "
        f"Média: {estudante['media']:.2f}"
    )

print("\n")
print("RESULTADO DA TURMA")

print(
    f"Maior média: "
    f"{maior_media['nome']} - {maior_media['media']:.2f}"
)

print(
    f"Menor média: "
    f"{menor_media['nome']} - {menor_media['media']:.2f}"
)

print(f"Aprovados:    {aprovados}")
print(f"Recuperação:  {recuperacao}")
print(f"Reprovados:   {reprovados}")