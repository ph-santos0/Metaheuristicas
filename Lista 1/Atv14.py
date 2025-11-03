def nomes_com_a(lista):
    return [nome for nome in lista if nome.startswith("A")]


nomes = ["Ana", "Bruno", "Amanda", "Carlos", "Alice"]
print("Nomes que começam com A:", nomes_com_a(nomes))
