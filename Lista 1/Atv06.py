pessoas = ()

for i in range(5):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input("Digite a idade: "))
    pessoas += ((nome, idade),)

print("\n--- DADOS CADASTRADOS ---")
for nome, idade in pessoas:
    print(f"Nome: {nome} | Idade: {idade}")

print("\n--- MAIORES DE IDADE ---")
for nome, idade in pessoas:
    if idade >= 18:
        print(nome)
