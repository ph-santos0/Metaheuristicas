populacao_a = 80000
populacao_b = 200000

taxa_a = 0.03
taxa_b = 0.015

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
print(f"População de A: {int(populacao_a)} habitantes")
print(f"População de B: {int(populacao_b)} habitantes")
