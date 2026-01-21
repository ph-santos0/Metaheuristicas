import pproducao as pp
import random
import statistics
import os
import time

# --- CONFIGURAÇÕES DO AG ---
TAMANHO_POPULACAO = 50      # Quantos indivíduos na população
NUM_GERACOES = 50           # Quantas gerações rodar
TAXA_CRUZAMENTO = 0.8       # Probabilidade de ocorrer crossover (80%)
TAXA_MUTACAO = 0.01         # Probabilidade de mutação por gene (1%)
TORNEIO_SIZE = 3            # Tamanho do torneio para seleção

# --- CARREGAMENTO DE DADOS ---
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_dados = os.path.join(diretorio_atual, 'dados.csv')

try:
    DADOS = pp.loadData(caminho_dados)
except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado em {caminho_dados}")
    exit()

def calcular_fitness(solucao):
    """Calcula VPL - Penalidade."""
    penalidade, vpl_total = pp.avaliaSolucao(DADOS, solucao)
    # Retornamos o valor líquido. Se for muito negativo, o AG vai evitar.
    return vpl_total - penalidade

def gerar_populacao_inicial(tamanho):
    """Cria uma lista de soluções aleatórias."""
    populacao = []
    for _ in range(tamanho):
        solucao = pp.getSolucaoAleatoria()
        populacao.append(solucao)
    return populacao

def selecao_torneio(populacao, fitnesses):
    """Seleciona um pai disputando um torneio entre K indivíduos aleatórios."""
    indices_competidores = random.sample(range(len(populacao)), TORNEIO_SIZE)
    
    # Encontra o índice do melhor entre os competidores
    melhor_idx = indices_competidores[0]
    melhor_fit = fitnesses[melhor_idx]
    
    for idx in indices_competidores[1:]:
        if fitnesses[idx] > melhor_fit:
            melhor_fit = fitnesses[idx]
            melhor_idx = idx
            
    return populacao[melhor_idx][:] # Retorna cópia do vencedor

def cruzamento_ponto_unico(pai1, pai2):
    """Realiza o crossover de 1 ponto (corta e troca metades)."""
    if random.random() < TAXA_CRUZAMENTO:
        # Escolhe um ponto de corte aleatório (evitando pontas)
        ponto_corte = random.randint(1, len(pai1) - 1)
        
        filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
        filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
        return filho1, filho2
    else:
        # Se não houver cruzamento, os filhos são cópias dos pais
        return pai1[:], pai2[:]

def mutacao(solucao):
    """Percorre cada gene (talhão) e tem chance de alterar a prescrição."""
    for i in range(len(solucao)):
        if random.random() < TAXA_MUTACAO:
            # Altera para uma nova prescrição aleatória (1 a 81)
            solucao[i] = random.randint(1, 81)
    return solucao

def executar_ag():
    # 1. Inicialização
    populacao = gerar_populacao_inicial(TAMANHO_POPULACAO)
    
    # Avalia a população inicial
    fitnesses = [calcular_fitness(ind) for ind in populacao]
    
    melhor_solucao_global = populacao[0][:]
    melhor_fitness_global = fitnesses[0]

    # Loop das Gerações
    for geracao in range(NUM_GERACOES):
        nova_populacao = []
        
        # Elitismo: Mantém o melhor da geração anterior intacto (Opcional, mas recomendado)
        idx_melhor = fitnesses.index(max(fitnesses))
        nova_populacao.append(populacao[idx_melhor][:]) # Adiciona o campeão
        
        # Verifica se o melhor atual supera o global
        if fitnesses[idx_melhor] > melhor_fitness_global:
            melhor_fitness_global = fitnesses[idx_melhor]
            melhor_solucao_global = populacao[idx_melhor][:]

        # Preenche o resto da nova população com filhos
        while len(nova_populacao) < TAMANHO_POPULACAO:
            # 2. Seleção
            pai1 = selecao_torneio(populacao, fitnesses)
            pai2 = selecao_torneio(populacao, fitnesses)
            
            # 3. Cruzamento
            filho1, filho2 = cruzamento_ponto_unico(pai1, pai2)
            
            # 4. Mutação
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)
            
            nova_populacao.append(filho1)
            if len(nova_populacao) < TAMANHO_POPULACAO:
                nova_populacao.append(filho2)
        
        # Atualiza a população e recalcula fitness
        populacao = nova_populacao
        fitnesses = [calcular_fitness(ind) for ind in populacao]

    # Checagem final do melhor resultado
    return melhor_fitness_global

# --- MAIN (30 Execuções) ---
if __name__ == "__main__":
    resultados = []
    print("\n" + "="*50)
    print("EXECUTANDO ALGORITMO GENÉTICO (30 VEZES)")
    print("="*50)
    
    tempo_inicio_total = time.time()
    
    for i in range(30):
        inicio_exec = time.time()
        res = executar_ag()
        resultados.append(res)
        fim_exec = time.time()
        print(f"Execução {i+1:02d}/30 | Fitness: {res:14.2f} | Tempo: {fim_exec - inicio_exec:.2f}s")

    tempo_total = time.time() - tempo_inicio_total

    # Relatório Estatístico
    print("\n" + "="*50)
    print("RELATÓRIO ESTATÍSTICO (ALGORITMO GENÉTICO)")
    print("="*50)
    print(f"Melhor Resultado:  {max(resultados):15.2f}")
    print(f"Pior Resultado:    {min(resultados):15.2f}")
    print(f"Média:             {statistics.mean(resultados):15.2f}")
    print(f"Desvio Padrão:     {statistics.stdev(resultados):15.2f}")
    print(f"Tempo Total:       {tempo_total:.2f}s")
    print("="*50)