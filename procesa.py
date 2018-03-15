import numpy as np
data = np.loadtxt('monthrg.dat')
tiempo = data[:,0]+(data[:,1]-1)/12.0
manchas = data[:,3]

cond = tiempo>=1900
tiempo = tiempo[cond]
manchas = manchas[cond]

resultado = np.array([tiempo, manchas])
np.savetxt('fecha_manchas.dat',resultado.T)
