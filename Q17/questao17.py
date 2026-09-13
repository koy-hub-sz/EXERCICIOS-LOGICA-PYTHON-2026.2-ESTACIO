import math

print(" CÁLCULOS MATEMÁTICOS")

while True:
    try:
        numero = float(
            input("Digite um número real: ").replace(",", ".")
        )
        break

    except ValueError:
        print("Erro: digite um número válido.")

valor_absoluto = abs(numero)

teto = math.ceil(numero)
piso = math.floor(numero)

print("\n")
print("RESULTADOS")

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"Raiz quadrada:       {raiz:.2f}")
else:
    print("Raiz quadrada:       não existe no conjunto dos reais.")

print(f"Valor absoluto:      {valor_absoluto:.2f}")
print(f"Arredondamento teto: {teto}")
print(f"Arredondamento piso: {piso}")

if numero.is_integer() and numero >= 0:
    numero_inteiro = int(numero)
    fatorial = math.factorial(numero_inteiro)

    print(f"Fatorial:            {fatorial}")
else:
    print(
        "Fatorial:            "
        "não pode ser calculado, pois o número não é "
        "um inteiro não negativo."
    )