print("     CONVERSOR DE TEMPERATURA")

while True:
    try:
        celsius = float(
            input("Digite a temperatura em Celsius (°C): ").replace(",", ".")
        )
        break
    except ValueError:
        print("Erro: digite uma temperatura válida.")

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print("\n")
print("RESULTADO:")
print(f"Celsius:    {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin:     {kelvin:.2f} K")