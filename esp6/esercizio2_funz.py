import numpy as np
import matplotlib.pyplot as plt
import sys


def random_walk_5p(step, N):
    
    for p in range(5):
        dx = np.array([0])
        dy = np.array([0])
        r = np.random.uniform(low = 0, high = 2*np.pi, size = N)
        k = 0
        j = 0
        for c in range(N):
            k = k + step*np.cos(r[c])
            j = j + step*np.sin(r[c])
            dx = np.append(dx , k)
            dy = np.append(dy , j)
        plt.plot(dx , dy)
    plt.ylabel(r'$\Delta y$')
    plt.xlabel(r'$\Delta x$')
    plt.show()

def random_walk_pAB(step, N):

    fig,ax = plt.subplots(1,2, figsize=(12,6))
    
    for p in range(5):
        dx = np.array([0])
        dy = np.array([0])
        d2 = np.array([0])
        PASSI = np.array([0])
        
        r = np.random.uniform(low = 0, high = 2*np.pi, size = N)
        k = 0
        j = 0
        for c in range(N):
            k = k + step*np.cos(r[c])
            j = j + step*np.sin(r[c])
            dx = np.append(dx , k)
            dy = np.append(dy , j)
            d2 = np.append(d2, k**2 + j**2)
            PASSI = np.append(PASSI,c+1)
            
       
        ax[0].plot(dx , dy)
        ax[1].plot(PASSI,d2)
                              
    ax[0].set_ylabel(r'$\Delta y$')
    ax[0].set_xlabel(r'$\Delta x$')

    ax[1].set_xlabel(r'Numero di passi')
    ax[1].set_ylabel(r'$Distanza^2$')
    plt.show()

