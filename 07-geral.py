# nome = input("Informe seu nome: ")
# print(nome)

# x = int(input("Informe um número inteiro: "))
# y = int(input("Informe outro número inteiro: "))
# z = x + y
# print("A soma é", z)

# a = float(input("Agora informe um número real: "))
# a /= 2
# print("A metade de", a * 2, "é", a)

# idade = int(input("Informe sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Menor de idade")
#     print("Aproveite sua juventude!")

# idade = int(input("Informe sua idade: "))
# if idade < 12:
#     print("Criança")
# elif idade < 18:
#     print("Adolescente")
# else:
#     print("Adulto")

# print("Você é maior de idade." if idade >= 18 else "Menor de idade.")

# match idade:
#     case 1:
#         print("Bebê")
#     case 7:
#         print("Criança")
#     case 18:
#         print("Adulto")
#     case _:
#         print("Desconhecido")

# i = 0
# while i < 10:
#     print("Fernando")
#     i = i + 1

# Com for
# inteiro = int(input("Informe um número inteiro positivo: "))
# fatorial = 1
# for i in range(1, inteiro + 1):
#     fatorial *= i
# print(fatorial)

# Com while
# inteiro = int(input("Informe um número inteiro positivo: "))
# fatorial = 1
# i = inteiro
# while i >= 1:
#     fatorial *= i
#     i -= 1
# print(fatorial)

# for i in range(1, 4):
#     print(i, "IFMG")

nomes = ["João", "Maria", "Pedro", "Ana"]
# for a in nomes:
#     print(a)

for i in range(len(nomes)):
    print(nomes[i])
