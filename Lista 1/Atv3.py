alunos = []
for i in range(10):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1} (0 a 10): "))
    alunos.append({"nome": nome, "nota": nota})

print("\nAlunos com média maior ou igual a 6:")
for aluno in alunos:
    if aluno["nota"] >= 6:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")
