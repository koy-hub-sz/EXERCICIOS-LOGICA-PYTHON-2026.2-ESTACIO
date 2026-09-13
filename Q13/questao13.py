print("AGENDA DE CONTATOS")

contatos = []

for i in range(1, 6):
    print(f"\n--- Cadastro do contato {i} ---")

    while True:
        nome = input("Nome: ").strip()

        if nome:
            break
        else:
            print("Erro: o nome não pode ficar vazio.")


    while True:
        telefone = input("Telefone: ").strip()

        if telefone:
            break
        else:
            print("Erro: o telefone não pode ficar vazio.")

    while True:
        email = input("E-mail: ").strip()

        if email:
            break
        else:
            print("Erro: o e-mail não pode ficar vazio.")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

print("             CONSULTA")

nome_consulta = input(
    "Digite o nome da pessoa que deseja consultar: "
).strip()

contato_encontrado = None

for contato in contatos:
    if contato["nome"].lower() == nome_consulta.lower():
        contato_encontrado = contato
        break

if contato_encontrado is not None:
    print("\nContato encontrado!")
    print("-" * 50)
    print(f"Nome:     {contato_encontrado['nome']}")
    print(f"Telefone: {contato_encontrado['telefone']}")
    print(f"E-mail:   {contato_encontrado['email']}")
    print("-" * 50)
else:
    print("\nContato não encontrado.")