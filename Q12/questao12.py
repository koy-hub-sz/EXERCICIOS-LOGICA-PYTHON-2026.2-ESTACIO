print("CONTROLE DE ESTOQUE")

produtos = []

for i in range(1, 6):
    print(f"\n Cadastro do produto {i}")

    while True:
        nome = input("Nome do produto: ").strip()

        if nome:
            break
        else:
            print("Erro: o nome não pode ficar vazio.")

    while True:
        try:
            preco = float(
                input("Preço unitário: R$ ").replace(",", ".")
            )

            if preco > 0:
                break
            else:
                print("Erro: o preço deve ser maior que zero.")

        except ValueError:
            print("Erro: digite um preço válido.")

    while True:
        try:
            quantidade = int(
                input("Quantidade em estoque: ")
            )

            if quantidade >= 0:
                break
            else:
                print("Erro: a quantidade não pode ser negativa.")

        except ValueError:
            print("Erro: digite uma quantidade inteira.")

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

valor_total_estoque = 0

for produto in produtos:
    valor_produto = produto["preco"] * produto["quantidade"]
    valor_total_estoque += valor_produto

produto_maior_preco = produtos[0]

for produto in produtos:
    if produto["preco"] > produto_maior_preco["preco"]:
        produto_maior_preco = produto

print("\n")
print("PRODUTOS CADASTRADOS")

for produto in produtos:
    valor_estoque = produto["preco"] * produto["quantidade"]

    print(f"Produto:     {produto['nome']}")
    print(f"Preço:       R$ {produto['preco']:.2f}")
    print(f"Quantidade:  {produto['quantidade']}")
    print(f"Valor total: R$ {valor_estoque:.2f}")

print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")

print("\nProduto com maior preço unitário:")
print(f"Nome:  {produto_maior_preco['nome']}")
print(f"Preço: R$ {produto_maior_preco['preco']:.2f}")