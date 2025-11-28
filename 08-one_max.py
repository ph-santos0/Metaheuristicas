import random

def gera_solucao(n):
    s = []
    i = 0
    while i < n:
        s.append(random.randint(0, 1))
        i += 1
    return s

def avalia_solucao(solucao):
    return sum(solucao)

def heuristica_aleatoria(n, iteracoes):
    melhor = None
    melhor_avaliacao = -1
    
    i = 0
    while i < iteracoes:
        solucao = gera_solucao(n)
        avaliacao = avalia_solucao(solucao)
        
        if avaliacao > melhor_avaliacao:
            melhor = solucao
            melhor_avaliacao = avaliacao
        
        i += 1
        
    return melhor, melhor_avaliacao

print(heuristica_aleatoria(10, 100))