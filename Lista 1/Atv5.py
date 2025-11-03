populacao_a = float(input("Informe a população do país A: "))
populacao_b = float(input("Informe a população do país B: "))

taxa_a = float(input("Informe a taxa de crescimento anual do país A (em %): ")) / 100
taxa_b = float(input("Informe a taxa de crescimento anual do país B (em %): ")) / 100

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f"\nSerão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
print(f"População final de A: {int(populacao_a)} habitantes")
print(f"População final de B: {int(populacao_b)} habitantes")
