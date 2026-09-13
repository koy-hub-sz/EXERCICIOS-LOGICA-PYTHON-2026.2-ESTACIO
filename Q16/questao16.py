numeros = []

while True:
    print("\n")
    print("GERENCIAMENTO DE NÚMEROS")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            try:
                numero = float(
                    input("Digite o número: ").replace(",", ".")
                )

                numeros.append(numero)
                print("Número cadastrado com sucesso!")
                break

            except ValueError:
                print("Erro: digite um número válido.")

    elif opcao == "2":
        if len(numeros) == 0:
            print("\nNenhum número cadastrado.")
        else:
            print("\nNúmeros cadastrados:")

            for i, numero in enumerate(numeros, start=1):
                print(f"{i} - {numero:g}")

    elif opcao == "3":
        if len(numeros) == 0:
            print("\nNenhum número cadastrado.")
        else:
            maior = numeros[0]

            for numero in numeros:
                if numero > maior:
                    maior = numero

            print(f"\nMaior número: {maior:g}")

    elif opcao == "4":
        if len(numeros) == 0:
            print("\nNenhum número cadastrado.")
        else:
            menor = numeros[0]

            for numero in numeros:
                if numero < menor:
                    menor = numero

            print(f"\nMenor número: {menor:g}")

    elif opcao == "5":
        if len(numeros) == 0:
            print("\nNenhum número cadastrado.")
        else:
            soma = sum(numeros)
            media = soma / len(numeros)

            print(f"\nMédia dos números: {media:.2f}")

    elif opcao == "0":
        print("\nPrograma encerrado. Até mais!")
        break

    else:
        print("\nErro: opção inválida. Escolha uma opção do menu.")