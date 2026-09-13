print("ESTATÍSTICA DE 10 NÚMEROS")

soma = 0
quantidade_positivos = 0
quantidade_negativos = 0
quantidade_pares = 0
quantidade_impares = 0

for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {i}º número inteiro: "))
            break
        except ValueError:
            print("Erro: digite apenas números inteiros.")

    soma += numero

    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1

    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

media = soma / 10

print("\n")
print("RELATÓRIO ESTATÍSTICO")
print(f"Soma dos números:        {soma}")
print(f"Números positivos:       {quantidade_positivos}")
print(f"Números negativos:       {quantidade_negativos}")
print(f"Números pares:           {quantidade_pares}")
print(f"Números ímpares:         {quantidade_impares}")
print(f"Média aritmética:        {media:.2f}")