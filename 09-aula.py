import math
import random

def bin2float(bits, a, b):
    g = 0
    n = len(bits)
    for i in range(n):
        g += bits[i] * (2 ** (n - 1 - i))

    return a + (g/(2**n - 1) * (b - a))

b = [1,0,1,0,1,]
print(bin2float(b, 0, 10))

def f(x,y):
    return (5 + math.sin(x) * math.sin(y) + 0,5 * math.sin(2*x) * math.sin(2*y) - 0.1 * (x**2 + y**2))

def gerasolucao(n):
    s = []
    i = 0
    while i < n:
        s.append(random.randint(0, 1))
        i += 1
    return s

def avaliasolucao(solucao):
    minx, maxx = -8, 8
    miny, maxy = -8, 8
    n = len(solucao)
    meio = n // 2
    solx = solucao[:meio]
    soly = solucao[meio:n]
    x = bin2float(solx, minx, maxx)
    y = bin2float(soly, miny, maxy)
    
    return f(x, y)

def hill_climbing(bits, maxit):
    sol_atual = gerasolucao(bits)
    fitness_atual = avaliasolucao(sol_atual)
    
    for _ in range(maxit):
        sol_vizinho = sol_atual.copy()
        r = random.randint(0, bits - 1)
        sol_vizinho[r] = 1 - sol_vizinho[r]
        fitness_vizinho = avaliasolucao(sol_vizinho)
        
        if fitness_vizinho > fitness_atual:
            sol_atual = sol_vizinho
            fitness_atual = fitness_vizinho
            
    return sol_atual, fitness_atual

sa, fa = hill_climbing(30, 1000)
print(sa)
print(fa)