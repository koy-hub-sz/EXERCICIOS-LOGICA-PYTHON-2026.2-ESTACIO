print("ORDENAÇÃO DE TRÊS NÚMEROS")

while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))
        numero3 = int(input("Digite o terceiro número inteiro: "))

        if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
            print("Erro: os três números devem ser distintos.")
        else:
            break

    except ValueError:
        print("Erro: digite apenas números inteiros.")

if numero1 > numero2:
    if numero1 > numero3:
        maior = numero1

        if numero2 > numero3:
            mediano = numero2
            menor = numero3
        else:
            mediano = numero3
            menor = numero2
    else:
        maior = numero3
        mediano = numero1
        menor = numero2
else:
    if numero2 > numero3:
        maior = numero2

        if numero1 > numero3:
            mediano = numero1
            menor = numero3
        else:
            mediano = numero3
            menor = numero1
    else:
        maior = numero3
        mediano = numero2
        menor = numero1

print("\n")
print("RESULTADO")
print(f"Maior número:        {maior}")
print(f"Número intermediário: {mediano}")
print(f"Menor número:        {menor}")