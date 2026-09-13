print("RELATÓRIO DE NÚMEROS")

numeros = []

for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {i}º número inteiro: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Erro: digite apenas números inteiros.")

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("\n")
print("RELATÓRIO")

print(f"Números informados: {numeros}")
print(f"Números pares:      {pares}")
print(f"Números ímpares:    {impares}")
print(f"Soma:               {soma}")
print(f"Média:              {media:.2f}")
print(f"Maior valor:        {maior}")
print(f"Menor valor:        {menor}")