# Carregando dados
import pproducao as ppr
dados = ppr.loadData("dados.csv")

s = ppr.getSolucaoAleatoria()
print(s)
ppr.DMIN = 1000
ppr.DMAX = 20000

print("Dmin: ", ppr.DMIN)
print("Dmax: ", ppr.DMAX)
p, vpl = ppr.avaliaSolucao(dados, s)

f = vpl - p

print("Penalidade: ", p)
print("VPL: ", vpl)
print("Funcao objetivo: ", f)