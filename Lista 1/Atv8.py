alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome == "sair":
        break
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

if alunos:
    media = sum(alunos.values()) / len(alunos)
    acima_da_media = [nome for nome, nota in alunos.items() if nota > media]
    maior_aluno = max(alunos, key=alunos.get)

    print(f"\nMédia da turma: {media:.2f}")
    print("\nAlunos acima da média:")
    for nome in acima_da_media:
        print(nome)
    print(
        f"\nAluno com a maior nota: {maior_aluno} ({alunos[maior_aluno]:.2f})")
else:
    print("Nenhum aluno foi cadastrado.")
