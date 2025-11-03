def apenas_pares(lista):
    return [num for num in lista if num % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print("Números pares da lista:", apenas_pares(numeros))
