import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,2, figsize = (11,5))

ar = np.random.uniform(low = 0, high = 10, size = 1000000)
ar2 = np.random.uniform(low = 0, high = 0.3, size = 1000000)

def legge1(x):

    #Funzione per generare la linea della funzione f(x) =3*x^2 / 1000
    #
    #
    #a = un array di zero
    #
    #sostituisco ad uno ad uno gli zero di a con i valori dati da f(x)
    #

    a = np.zeros(len(x))
    
    a = 3*(x**2)/1000
    
    return a

y = ar2 <= legge1(ar)
#y è un insieme di booleani PERCHE è una maschera

ax[0].hist(ar[y], bins = 1000, range=(0,10),  color = 'red')
ax[0].set_title('Distribuzione secondo la funzione (Hit or miss)')
ax[0].set_xlabel('x')



a0 = np.random.uniform(low=0, high =10, size = 1000000)
a1 = np.random.random(1000000)

def inv_leggec(y):

    b = np.zeros(len(y))
    b = (1000*y)**0.33

    return b



ax[1].hist(inv_leggec(a1), bins=1000, range=(0,10), color='orange')
ax[1].set_title('Distribuzione secondo la funzione (Cumulativa)')
ax[1].set_xlabel('x')
plt.show()

