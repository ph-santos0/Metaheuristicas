matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\n--- MATRIZ 5x5 ---")
for linha in matriz:
    for valor in linha:
        print(f"{valor:4}", end="")
    print()
