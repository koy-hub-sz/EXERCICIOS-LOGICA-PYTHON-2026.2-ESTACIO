print("ANÁLISE DE SINAL E PARIDADE")

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Erro: digite apenas um número inteiro.")

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "nulo"

if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print("\n")
print(f"O número {numero} é {sinal} e {paridade}.")