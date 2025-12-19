import random

# Definindo uma função que gera uma solução inicial aleatória
def generate_initial_solution(size):
    return [random.randint(0, 1) for _ in range(size)]

# Função de avaliação: conta o número de 1s na solução
def evaluate(solution):
    return sum(solution)

# Gera uma nova solução invertendo 'n' bits aleatórios
def neighborhood_flip(solution, n):
    new_solution = solution.copy()
    indices = random.sample(range(len(solution)), n)
    for index in indices:
        new_solution[index] = 1 - new_solution[index]  # Inverte o bit
    return new_solution

# Busca local: tenta melhorar a solução corrente usando uma estrutura de vizinhança simples
def local_search(solution):
    best_solution = solution
    best_score = evaluate(solution)
    for i in range(1, len(solution) + 1):  # Inverte 1 até todos os bits
        new_solution = neighborhood_flip(solution, i)
        new_score = evaluate(new_solution)
        if new_score > best_score:
            best_solution, best_score = new_solution, new_score
    return best_solution

# Algoritmo VNS para o problema MaxOne
def VNS(size, max_iterations, max_no_improve, max_neighborhood):
    current_solution = generate_initial_solution(size)
    current_score = evaluate(current_solution)
    
    iterations = 0
    no_improve = 0
    
    while iterations < max_iterations and no_improve < max_no_improve:
        neighborhood = 1
        while neighborhood <= max_neighborhood:
            # Gera uma nova solução a partir da vizinhança
            new_solution = neighborhood_flip(current_solution, neighborhood)
            # Aplica busca local
            new_solution = local_search(new_solution)
            new_score = evaluate(new_solution)
            
            if new_score > current_score:
                current_solution, current_score = new_solution, new_score
                no_improve = 0  # Reseta o contador de estagnação
                neighborhood = 1  # Reinicia a vizinhança
            else:
                neighborhood += 1
        
        iterations += 1
        no_improve += 1

    return current_solution, current_score

# Parâmetros
size = 20  # Tamanho da string binária
max_iterations = 100
max_no_improve = 10
max_neighborhood = 5

# Executa o VNS
best_solution, best_score = VNS(size, max_iterations, max_no_improve, max_neighborhood)
print(f"Melhor solução encontrada: {best_solution}")
print(f"Pontuação da melhor solução: {best_score}")