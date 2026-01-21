import pproducao as pp
import random
import statistics
import os
import time

# --- CONFIGURAÇÕES DO HILL CLIMBING ---
# Como não podemos testar todos os 9.600 vizinhos a cada passo,
# definimos uma "paciência". Se o algoritmo tentar gerar um vizinho
# X vezes e não achar ninguém melhor, assumimos que chegou no topo.
PACIENCIA_MAXIMA = 500  

# --- CARREGAMENTO DE DADOS ---
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_dados = os.path.join(diretorio_atual, 'dados.csv')

try:
    DADOS = pp.loadData(caminho_dados)
except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado em {caminho_dados}")
    exit()

def calcular_fitness(solucao):
    """
    Calcula o valor da solução (VPL - Penalidade).
    Retorna apenas o valor líquido.
    """
    penalidade, vpl_total = pp.avaliaSolucao(DADOS, solucao)
    return vpl_total - penalidade

def gerar_vizinho_aleatorio(solucao_atual):
    """
    Gera UM vizinho alterando aleatoriamente a prescrição de UM talhão.
    """
    vizinho = solucao_atual[:] # Cria uma cópia
    
    # Escolhe um talhão aleatório (0 a 119)
    idx_talhao = random.randint(0, 119)
    
    # Escolhe uma nova prescrição aleatória (1 a 81)
    # Garante que a nova prescrição seja diferente da atual
    prescricao_atual = vizinho[idx_talhao]
    nova_prescricao = prescricao_atual
    while nova_prescricao == prescricao_atual:
        nova_prescricao = random.randint(1, 81)
        
    vizinho[idx_talhao] = nova_prescricao
    return vizinho

def executar_hill_climbing():
    # 1. Solução Inicial Aleatória
    solucao_atual = pp.getSolucaoAleatoria()
    fitness_atual = calcular_fitness(solucao_atual)
    
    tentativas_sem_melhora = 0
    
    # Loop Principal: Continua enquanto tiver paciência
    while tentativas_sem_melhora < PACIENCIA_MAXIMA:
        
        # 2. Gera um candidato a vizinho
        vizinho = gerar_vizinho_aleatorio(solucao_atual)
        fitness_vizinho = calcular_fitness(vizinho)
        
        # 3. Critério de Aceitação (Apenas Melhora Estrita)
        if fitness_vizinho > fitness_atual:
            # Achou um vizinho melhor! Move para ele.
            solucao_atual = vizinho[:]
            fitness_atual = fitness_vizinho
            
            # Reseta a paciência, pois ainda estamos subindo o morro
            tentativas_sem_melhora = 0
        else:
            # Vizinho é pior ou igual. Gasta a paciência.
            tentativas_sem_melhora += 1
            
    # Se a paciência acabou, assumimos que estamos num Ótimo Local
    return fitness_atual

# --- MAIN (30 Execuções) ---
if __name__ == "__main__":
    resultados = []
    print("\n" + "="*50)
    print("EXECUTANDO HILL CLIMBING ESTOCÁSTICO (30 VEZES)")
    print("="*50)
    
    tempo_inicio_total = time.time()
    
    for i in range(30):
        inicio_exec = time.time()
        
        res = executar_hill_climbing()
        resultados.append(res)
        
        fim_exec = time.time()
        print(f"Execução {i+1:02d}/30 | Fitness: {res:14.2f} | Tempo: {fim_exec - inicio_exec:.2f}s")

    tempo_total = time.time() - tempo_inicio_total

    # Relatório Estatístico
    print("\n" + "="*50)
    print("RELATÓRIO ESTATÍSTICO (HILL CLIMBING)")
    print("="*50)
    print(f"Melhor Resultado:  {max(resultados):15.2f}")
    print(f"Pior Resultado:    {min(resultados):15.2f}")
    print(f"Média:             {statistics.mean(resultados):15.2f}")
    print(f"Desvio Padrão:     {statistics.stdev(resultados):15.2f}")
    print(f"Tempo Total:       {tempo_total:.2f}s")
    print("="*50)