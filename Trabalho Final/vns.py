import pproducao as ppr
import random
import statistics
import os
import time  # Importado para calcular o tempo

diretorio = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO = os.path.join(diretorio, 'dados.csv')

try:
    dados = ppr.loadData(NOME_ARQUIVO)
except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado em {NOME_ARQUIVO}")
    exit()

def calcular_fitness(solucao):
    penalidade, vpl = ppr.avaliaSolucao(dados, solucao)
    return vpl - penalidade

def shake(solucao, k):
    """Agitação: Altera 'k' talhões aleatórios."""
    nova_sol = list(solucao)
    for _ in range(k):
        nova_sol[random.randint(0, 119)] = random.randint(1, 81)
    return nova_sol

def executar_vns(total_avaliacoes=5000):
    """Busca em vizinhanças variáveis."""
    s = ppr.getSolucaoAleatoria()
    melhor_f = calcular_fitness(s)
    cont = 1
    
    while cont < total_avaliacoes:
        k = 1
        while k <= 2 and cont < total_avaliacoes:
            s_viz = shake(s, k) # Shake (Agitação)
            f_viz = calcular_fitness(s_viz)
            cont += 1
            
            if f_viz > melhor_f: # Se melhorou, aceita e reseta k
                s, melhor_f = s_viz, f_viz
                k = 1
            else: # Se não melhorou, aumenta a intensidade
                k += 1
    return melhor_f

# MAIN (30 Execuções)
if __name__ == "__main__":
    resultados = []
    
    print("\n" + "="*50)
    print("EXECUTANDO ALGORITMO: VNS (REDUCED)")
    print("="*50)
    
    tempo_inicio_global = time.time()
    
    for i in range(30):
        inicio_exec = time.time()
        
        res = executar_vns()
        resultados.append(res)
        
        fim_exec = time.time()
        print(f"Execução {i+1:02d}/30 | Fitness: {res:14.2f} | Tempo: {fim_exec - inicio_exec:.2f}s")

    tempo_total = time.time() - tempo_inicio_global

    # Cálculos Estatísticos
    media = statistics.mean(resultados)
    desvio_padrao = statistics.stdev(resultados)
    melhor = max(resultados)
    pior = min(resultados)

    # RELATÓRIO ESTATÍSTICO PADRONIZADO
    print("\n" + "="*50)
    print("RELATÓRIO ESTATÍSTICO (VNS)")
    print("="*50)
    print(f"Melhor Resultado:  {melhor:15.2f}")
    print(f"Pior Resultado:    {pior:15.2f}")
    print(f"Média:             {media:15.2f}")
    print(f"Desvio Padrão:     {desvio_padrao:15.2f}")
    print(f"Tempo Total:       {tempo_total:.2f}s")
    print("="*50)