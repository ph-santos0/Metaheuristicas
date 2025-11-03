frutas = set()
repetidas = 0

while True:
    fruta = input("Digite o nome de uma fruta (ou 'sair' para encerrar): ")
    if fruta == "sair":
        break
    if fruta in frutas:
        repetidas += 1
    else:
        frutas.add(fruta)

print("\n--- FRUTAS CADASTRADAS ---")
for f in frutas:
    print(f)

print(f"\nTotal de frutas diferentes: {len(frutas)}")
print(f"Frutas não cadastradas (repetidas): {repetidas}")
