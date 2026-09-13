print("TABUADA")

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Erro: digite apenas um número inteiro.")

print("\n" + "=" * 40)
print(f"TABUADA DO {numero}")
print("=" * 40)

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")