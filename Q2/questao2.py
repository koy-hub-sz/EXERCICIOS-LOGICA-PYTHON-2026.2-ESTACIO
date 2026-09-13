print("CALCULADORA ARITMÉTICA")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
potenciacao = numero1 ** numero2


print("---------------------------")
print(f"Adição:           {adicao}")
print(f"Subtração:        {subtracao}")
print(f"Multiplicação:    {multiplicacao}")
print(f"Potenciação:      {potenciacao}")


if numero2 == 0:
    print("Divisão:         Divisão por zero não permitida")
    print("Divisão inteira: Divisão por zero não permitida")
    print("Resto da divisão: Divisão por zero não permitida")
else:
    divisao = numero1 / numero2
    divisao_inteira = numero1 // numero2
    resto = numero1 % numero2

    print(f"Divisão:          {divisao}")
    print(f"Divisão inteira:  {divisao_inteira}")
    print(f"Resto da divisão: {resto}")