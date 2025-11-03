matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

identidade = True
for i in range(5):
    for j in range(5):
        if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
            identidade = False

print("\n--- MATRIZ DIGITADA ---")
for linha in matriz:
    for valor in linha:
        print(f"{valor:3}", end="")
    print()

if identidade:
    print("\nA matriz é uma matriz identidade.")
else:
    print("\nA matriz NÃO é uma matriz identidade.")
