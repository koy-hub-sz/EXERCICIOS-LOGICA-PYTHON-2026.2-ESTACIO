print("ANÁLISE DE TEMPERATURAS")

temperaturas = []

for dia in range(1, 8):
    while True:
        try:
            temperatura = float(
                input(f"Digite a temperatura do {dia}º dia: ").replace(",", ".")
            )
            temperaturas.append(temperatura)
            break
        except ValueError:
            print("Erro: digite uma temperatura válida.")

maior_temperatura = temperaturas[0]
menor_temperatura = temperaturas[0]

for temperatura in temperaturas:
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

soma_temperaturas = sum(temperaturas)
media = soma_temperaturas / len(temperaturas)

dias_acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        dias_acima_media += 1

print("\n")
print("RELATÓRIO SEMANAL")

print("Temperaturas registradas:")

for i in range(len(temperaturas)):
    print(f"Dia {i + 1}: {temperaturas[i]:.2f} °C")

print(f"Maior temperatura:       {maior_temperatura:.2f} °C")
print(f"Menor temperatura:       {menor_temperatura:.2f} °C")
print(f"Temperatura média:       {media:.2f} °C")
print(f"Dias acima da média:     {dias_acima_media}")