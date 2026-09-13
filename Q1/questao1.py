# Questão 01 - Cadastro e apresentação de perfil pessoal

print("CADASTRO DE PERFIL")

nome = input("Digite seu nome completo: ").strip()

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade >= 0:
            break
        else:
            print("Erro: a idade não pode ser negativa.")
    except ValueError:
        print("Erro: digite uma idade válida usando números inteiros.")


while True:
    try:
        altura = float(input("Digite sua altura em metros: ").replace(",", "."))

        if altura > 0:
            break
        else:
            print("Erro: a altura deve ser maior que zero.")
    except ValueError:
        print("Erro: digite uma altura válida.")


cidade = input("Digite a cidade onde reside: ").strip()


print("CARTÃO DE IDENTIFICAÇÃO")
print(f"{'Nome:':<15} {nome}")
print(f"{'Idade:':<15} {idade} anos")
print(f"{'Altura:':<15} {altura:.2f} m")
print(f"{'Cidade:':<15} {cidade}")