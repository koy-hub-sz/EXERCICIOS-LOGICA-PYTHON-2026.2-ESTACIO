import random

print("SIMULAÇÃO DE LANÇAMENTO DE DADOS")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1 + dado2

print("\n LANÇAMENTO ÚNICO")
print(f"Primeiro dado: {dado1}")
print(f"Segundo dado:  {dado2}")
print(f"Soma:          {soma}")

print("\n 10 LANÇAMENTOS")

quantidade_somas_7 = 0

for lancamento in range(1, 11):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    print(
        f"Lançamento {lancamento:2}: "
        f"Dado 1 = {dado1} | "
        f"Dado 2 = {dado2} | "
        f"Soma = {soma}"
    )

    if soma == 7:
        quantidade_somas_7 += 1

print("\n")
print("RESULTADO")
print(f"A soma dos dados foi 7 em {quantidade_somas_7} lançamento(s).")