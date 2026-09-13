print("CLASSIFICAÇÃO ETÁRIA")

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade >= 0:
            break
        else:
            print("Erro: a idade não pode ser negativa.")

    except ValueError:
        print("Erro: digite uma idade válida usando números inteiros.")

if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print("\n")
print("RESULTADO")
print(f"Idade:          {idade} anos")
print(f"Classificação:  {classificacao}")