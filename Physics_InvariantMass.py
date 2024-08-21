import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd              
import os
import numpy
from numpy import genfromtxt

#Gráfico que nos auxilie a identificar uma partícula a partir de um dos processos de decaimento. 
#Nesse caso, nós vamos dizer que uma partícula pesada X decaiu em dois múons.
#X -> u*u

pasta = "C:\Tabelas"
ds = pd.read_csv("C:\Tabelas\example_allEvents.csv")
print(ds.columns)

#Selecionar então os nomes das colunas baseado no passo anterior:
ds = ds[['px1', 'py1', 'pz1', 'E1', 'px2', 'py2', 'pz2', 'E2']]

#Selecionar momentum em x da partícula 1:
px1=ds[["px1"]].to_numpy()
print(px1)

#Selecionar momentum em x da partícula 1:
py1=ds[["py1"]].to_numpy()
print(py1)

#Selecionar momentum em x da partícula 1:
pz1=ds[["pz1"]].to_numpy()
print(pz1)

#Selecionar momentum em x da partícula 1:
E1=ds[["E1"]].to_numpy()
print(E1)

#Selecionar momentum em x da partícula 1:
px2=ds[["px2"]].to_numpy()
print(px2)

#Selecionar momentum em x da partícula 1:
py2=ds[["py2"]].to_numpy()
print(py2)

#Selecionar momentum em x da partícula 1:
pz2=ds[["pz2"]].to_numpy()
print(pz2)

#Selecionar momentum em x da partícula 1:
E2=ds[["E2"]].to_numpy()
print(E2)

#Contruir a expressão da "Massa Invariante" e armazenar a informação
#onde  m1,2  é a massa do múon, equivalente a  mμ=0.10566  GeV.

m1 = 0.10566
m2 = 0.10566

ma = numpy.sqrt(m1**2 + m2**2 + 2*(E1*E2 - px1*px2 - py1*py2 - pz1*pz2))

hist1 = ma

histograma1, bins, _ = plt.hist(hist1, bins=60, range=[0, 100.4],
                                histtype = 'stepfilled', fc="b",
                                alpha=0.6,
                                label='Massa x Número de Eventos',
                                color = 'blue', linewidth=1.2)
plt.ylabel("Massa", fontsize=20)
plt.xlabel("Número de Eventos", fontsize=20)
plt.yscale('linear')
plt.xticks(range(1,100,4), fontsize = 18)
plt.gcf().set_size_inches(20, 10)
plt.legend(loc='upper right', prop={'size': 20})
plt.yticks(fontsize = 18)

fig = plt.gcf()
plt.show()
fig.savefig('massaInvariante.png', format='png', bbox_inches='tight')
