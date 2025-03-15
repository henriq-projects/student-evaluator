print("Bem-vindo ao aprovador de alunos!")

media = int(input("Digite a média mínima para aprovação: "))

while True:
    nome = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break  # Sai do loop se o usuário digitar "sair"
    
    try:
        nota = float(input("Agora digite sua nota: "))
    except ValueError:
        print("Favor, digite um número válido.")
        continue
    if nota >= media:
        print(f"O aluno {nome} passou!")
    else:
        print(f"O aluno {nome} não passou.")

print("Programa encerrado.")
