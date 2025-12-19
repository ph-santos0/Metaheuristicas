import csv;
import random;

"""
    DEFINIÇÕES DO PROBLEMA
"""
DMIN  = 140000; #Demanda Mínima
DMAX  = 150000; #Demanda Máxima
PMPM  = 500;   #Penalidade monetária por metro cúbico

"""
    MÉTODOS DE MANIPULAÇÃO DA BASE DE DADOS
"""
#Função para carregar os dados da base de dados
def loadData (fileName):
    data = [];
    with open(fileName, 'r') as file:
        CSVReader = csv.reader(file);
        for line in CSVReader:
            # Converte os valores da linha de string para inteiros
            array = [int(num) for num in line];
            data.append(array);
    return data;


#Retorna um array com o histórico de produção de 16 anos: uma linha das colunas 4 .. 19 da base de dados
def getHistoricoProducao (dados, talhao, prescricao):
    return dados[ (talhao - 1)*81 + prescricao-1][3:19 ];


#Retorna o VPL coluna 19 da base de dados
def getVPL (dados, talhao, prescricao):
    return dados[(talhao - 1)*81 + prescricao-1][19];


"""
    MÉTODOS DE MODELAGEM DA SOLUÇÃO
"""

#Retorna uma solução aleatória
def getSolucaoAleatoria ():
    res = []
    for i in range(120):
        res.append( random.randint(1,81) );
    return res;

"""
    MÉTODOS DE AVALIAÇÃO DE UMA SOLUÇÃO (VETOR DE PRESCRICOES)
"""
# retorna a matriz de produção, que é uma matriz de 120 linhas e 16 colunas contendo as produções por talhão, por ano
def getMatrizProducao (dados, prescricoes):
    matrizProducao = []
    talhao = 1
    for p in prescricoes:
        historicoProducao = getHistoricoProducao(dados, talhao, p);
        matrizProducao.append ( historicoProducao.copy()  );
        talhao = talhao + 1;

    return matrizProducao;

def getVetorVPL (dados, prescricoes):
    vetorVPL = []
    talhao = 1
    for p in prescricoes:
        VPL = getVPL(dados, talhao, p);
        vetorVPL.append ( VPL  );
        talhao = talhao + 1;

    return vetorVPL;


#Retorna um vetor contendo a produção total por ano
# matrizProducao é uma matriz de 120 linhas e 16 colunas contendo as produções por talhão, por ano
def getProducaoPorAno (matrizProducao):
    producaoPorAno = [];

    # Inicializa um vetor de somas com zeros com o mesmo tamanho que o número de colunas
    producaoPorAno = [0] * len(matrizProducao[0]);

    # Itera sobre as linhas da matriz
    for producao in matrizProducao:
        # Itera sobre os elementos da linha e soma nas colunas correspondentes
        for i, x in enumerate(producao):
            producaoPorAno[i] += x;
            
    return producaoPorAno;


# Retorna a soma dos VPL's de cada prescrição.
def getVPLTotal ( vetorVPL ):
    vplTotal = 0;
    for vpl in vetorVPL:
        vplTotal += vpl;
        
    return vplTotal;

def calculaPenalidade ( producaoPorAno ):
    p = 0;
    for producao in producaoPorAno:
        if producao < DMIN:
            p += (DMIN - producao) * PMPM;

        if producao > DMAX:
            p += (producao - DMAX) * PMPM;

    return p;


#Avalia uma solução retornando a penalidade e o VPL total
def avaliaSolucao ( dados, prescricoes ):
    
    #print('SOLUÇÃO');
    #print(prescricoes);

    #1) Calcular a matriz de produção
    matrizProducao = getMatrizProducao(dados, prescricoes);
    #print ('MATRIZ PRODUÇÃO')
    #print(matrizProducao)

    #2) Obter o VLPTotal
    vetorVPL = getVetorVPL(dados, prescricoes);
    #print ('VETOR VPL')
    #print(vetorVPL)

    VPLTotal = getVPLTotal(vetorVPL);
    #print ('VPL TOTAL')
    #print(VPLTotal)

    #3) Calcular a produção por ano
    producaoPorAno = getProducaoPorAno(matrizProducao);

    #4 Calcular a penalidade
    penalidade = calculaPenalidade ( producaoPorAno );
    #print ('PENALIDADE')
    #print(penalidade)


    #Retornar a penalidade e o VPL Total
    return penalidade, VPLTotal;