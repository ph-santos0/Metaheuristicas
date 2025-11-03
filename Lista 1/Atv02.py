print("Cinema - Verificação de Desconto")
ingresso = 38.76
print("Valor original do ingresso: " + str(ingresso))
idade = int(input("Digite sua idade: "))
if idade >= 12 and idade <= 60:
    print("Você não tem direito a desconto.")
else:
    print("Você tem direito a desconto.")
    ingresso = ingresso / 2

print("Valor do ingresso de acordo com sua idade: " + str(ingresso))
