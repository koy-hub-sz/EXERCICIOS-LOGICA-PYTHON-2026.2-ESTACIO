def ler_nome(mensagem):

    while True:
        nome = input(mensagem).strip()

        if nome:
            return nome
        else:
            print("Erro: o campo não pode ficar vazio.")

def ler_idade(mensagem):

    while True:
        try:
            idade = int(input(mensagem))

            if idade > 0:
                return idade
            else:
                print("Erro: a idade deve ser maior que zero.")

        except ValueError:
            print("Erro: digite uma idade inteira válida.")


def ler_nota(mensagem):

    while True:
        try:
            nota = float(
                input(mensagem).replace(",", ".")
            )

            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("Erro: digite uma nota válida.")

def calcular_media(notas):

    return sum(notas) / len(notas)


def determinar_situacao(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def buscar_estudante(estudantes, nome):

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            return estudante

    return None


def exibir_estudante(estudante):

    print(f"Nome:       {estudante['nome']}")
    print(f"Idade:      {estudante['idade']} anos")
    print(f"Curso:      {estudante['curso']}")

    print(f"Nota 1:     {estudante['notas'][0]:.2f}")
    print(f"Nota 2:     {estudante['notas'][1]:.2f}")
    print(f"Nota 3:     {estudante['notas'][2]:.2f}")

    print(f"Média:      {estudante['media']:.2f}")
    print(f"Situação:   {estudante['situacao']}")

def cadastrar_estudante(estudantes):

    print("\n")
    print("CADASTRO DE ESTUDANTE")

    nome = ler_nome("Nome: ")

    if buscar_estudante(estudantes, nome) is not None:
        print("Erro: já existe um estudante com esse nome.")
        return

    idade = ler_idade("Idade: ")
    curso = ler_nome("Curso: ")

    print("\nDigite as três notas:")
    nota1 = ler_nota("Nota 1: ")
    nota2 = ler_nota("Nota 2: ")
    nota3 = ler_nota("Nota 3: ")

    notas = (nota1, nota2, nota3)

    media = calcular_media(notas)
    situacao = determinar_situacao(media)

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    estudantes.append(estudante)

    print("\nEstudante cadastrado com sucesso!")

def listar_estudantes(estudantes):

    print("\n")
    print("LISTA DE ESTUDANTES")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    for numero, estudante in enumerate(estudantes, start=1):

        print(
            f"{numero} - {estudante['nome']} | "
            f"Curso: {estudante['curso']} | "
            f"Média: {estudante['media']:.2f} | "
            f"{estudante['situacao']}"
        )

def consultar_estudante(estudantes):

    print("\n")
    print("CONSULTAR ESTUDANTE")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome = ler_nome("Digite o nome do estudante: ")

    estudante = buscar_estudante(estudantes, nome)

    if estudante is not None:
        print("\nEstudante encontrado!")
        exibir_estudante(estudante)
    else:
        print("Estudante não encontrado.")

def alterar_dados(estudantes):

    print("\n")
    print("ALTERAR DADOS")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome = ler_nome("Digite o nome do estudante: ")

    estudante = buscar_estudante(estudantes, nome)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    print("\nEstudante encontrado:")
    exibir_estudante(estudante)

    while True:

        print("\nO que deseja alterar?")
        print("1 - Nome")
        print("2 - Idade")
        print("3 - Curso")
        print("4 - Notas")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            novo_nome = ler_nome("Novo nome: ")

            outro_estudante = buscar_estudante(
                estudantes, novo_nome
            )

            if outro_estudante is not None and outro_estudante != estudante:
                print("Erro: esse nome já está cadastrado.")
            else:
                estudante["nome"] = novo_nome
                print("Nome alterado com sucesso.")

        elif opcao == "2":

            estudante["idade"] = ler_idade("Nova idade: ")
            print("Idade alterada com sucesso.")

        elif opcao == "3":

            estudante["curso"] = ler_nome("Novo curso: ")
            print("Curso alterado com sucesso.")

        elif opcao == "4":

            print("\nDigite as novas notas:")

            nota1 = ler_nota("Nova nota 1: ")
            nota2 = ler_nota("Nova nota 2: ")
            nota3 = ler_nota("Nova nota 3: ")

            estudante["notas"] = (nota1, nota2, nota3)

            estudante["media"] = calcular_media(
                estudante["notas"]
            )

            estudante["situacao"] = determinar_situacao(
                estudante["media"]
            )

            print("Notas alteradas com sucesso.")

        elif opcao == "0":
            break

        else:
            print("Erro: opção inválida.")

def remover_estudante(estudantes):

    print("\n")
    print("REMOVER ESTUDANTE")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome = ler_nome("Digite o nome do estudante: ")

    estudante = buscar_estudante(estudantes, nome)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    print("\nEstudante selecionado:")
    exibir_estudante(estudante)

    while True:

        confirmacao = input(
            "Deseja realmente remover? (S/N): "
        ).strip().lower()

        if confirmacao == "s":

            estudantes.remove(estudante)

            print("Estudante removido com sucesso.")
            break

        elif confirmacao == "n":

            print("Operação cancelada.")
            break

        else:
            print("Digite apenas S para sim ou N para não.")

def gerar_relatorio(estudantes):

    print("\n")
    print("RELATÓRIO DA TURMA")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    maior_media = estudantes[0]
    menor_media = estudantes[0]

    soma_medias = 0

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:

        media = estudante["media"]

        soma_medias += media

        if media > maior_media["media"]:
            maior_media = estudante

        if media < menor_media["media"]:
            menor_media = estudante

        if media >= 7:
            aprovados += 1

        elif media >= 5:
            recuperacao += 1

        else:
            reprovados += 1

    media_geral = soma_medias / len(estudantes)

    print(f"Total de estudantes: {len(estudantes)}")

    print(
        f"Maior média: "
        f"{maior_media['nome']} - "
        f"{maior_media['media']:.2f}"
    )

    print(
        f"Menor média: "
        f"{menor_media['nome']} - "
        f"{menor_media['media']:.2f}"
    )

    print(f"Média geral: {media_geral:.2f}")

    print(f"Aprovados:   {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados:  {reprovados}")

estudantes = []

while True:

    print("\n")
    print("SISTEMA ACADÊMICO")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_estudante(estudantes)

    elif opcao == "2":
        listar_estudantes(estudantes)

    elif opcao == "3":
        consultar_estudante(estudantes)

    elif opcao == "4":
        alterar_dados(estudantes)

    elif opcao == "5":
        remover_estudante(estudantes)

    elif opcao == "6":
        gerar_relatorio(estudantes)

    elif opcao == "0":
        print("\nSistema encerrado. Até mais!")
        break

    else:
        print("\nErro: opção inválida. Tente novamente.")