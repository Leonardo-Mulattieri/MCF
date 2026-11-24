import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import argparse

x_0 = 4
m = 1
N = 10000

def parse_arguments():
    parse.add_argument('-b', '--opzione1', action = 'store_true', help =' Esempio di opzione booleana')

def V(x):
    k = 0.1
    return k*x**6

def V2(x):
    k = 0.1
    return k*x**2

def V3(x):
    k = 0.1
    return k*x**4

def V4(x):
    k = 0.1
    return k*abs(x)**(3/2)

def f1(x, xd):
    return 1/((V(xd) - V(x))**0.5)

def f2(x, xd):
    return 1/((V2(xd) - V2(x))**0.5)

def f3(x, xd):
    return 1/((V3(xd) - V3(x))**0.5)

def f4(x, xd):
    return 1/((V4(xd) - V4(x))**0.5)


def integrale( f , V , xd, N = N):
    s = np.linspace(0 , x_0**0.5 , N)
    g = np.empty(len(s))
    g[1:] = 2*s[1:] * f(xd - s[1:]**2 , xd)

    h = xd*1e-6
    dV = (V(xd) - V(xd - h)) / h        
    g[0] = 2/(dV**0.5)

    return integrate.simpson(g, dx= xd**0.5/(N-1) )


Cost = ((8*m)**0.5)

Periodo1 = Cost*(integrale(f1, V , x_0))
Periodo2 = Cost*(integrale(f2, V2, x_0)) 

#print(Periodo1, Periodo2, Periodo1-Periodo2)


#Parte grafica


def periodg1(xd, M =10000):

    #cambio la forma dell'integrale per evitare 
    s = np.linspace(0, (xd**0.5), M)
    f = np.empty(len(s))
    f[1:] = 2*s[1:] / (V(xd) - V(xd - s[1:]**2))**0.5

    #limite (=  2/sqrt(V(xd))) per evitare di ottenere 0/0

    h = xd*1e-6
    dV = (V(xd) - V(xd - h)) / h        
    f[0] = 2/(dV**0.5)

    return Cost * integrate.simpson(f, x=s)


def periodg2(xd, M = 10000):
    
    s = np.linspace(0, (xd**0.5), M)
    f = np.empty(len(s))
    f[1:] = 2*s[1:] / (V2(xd) - V2(xd - s[1:]**2))**0.5

    #limite (=  2/sqrt(V(xd))) per evitare di ottenere 0/0

    h = xd*1e-6
    dV = (V2(xd) - V2(xd - h)) / h        
    f[0] = 2/(dV**0.5)
    
    return Cost * integrate.simpson(f, x=s)


def periodg3(xd, M = 10000):
    
    s = np.linspace(0, (xd**0.5), M)
    f = np.empty(len(s))
    f[1:] = 2*s[1:] / (V3(xd) - V3(xd - s[1:]**2))**0.5

    #limite (=  2/sqrt(V(xd))) per evitare di ottenere 0/0

    h = xd*1e-6
    dV = (V3(xd) - V3(xd - h)) / h        
    f[0] = 2/(dV**0.5)
    
    return Cost * integrate.simpson(f,x=s)

def periodg4(xd, M = 10000):
    
    s = np.linspace(0, (xd**0.5), M)
    f = np.empty(len(s))
    f[1:] = 2*s[1:] / (V4(xd) - V4(xd - s[1:]**2))**0.5

    #limite (=  2/sqrt(V(xd))) per evitare di ottenere 0/0

    h = xd*1e-6
    dV = (V4(xd) - V4(xd - h)) / h        
    f[0] = 2/(dV**0.5)
    
    return Cost * integrate.simpson(f, x=s)


x_d = np.linspace(x_0/N, x_0, N)


#fondo il ciclo for all'intero dell'array
T1 = np.array([periodg1(xd) for xd in x_d]) 
T2 = np.array([periodg2(xd) for xd in x_d])
T3 = np.array([periodg3(xd) for xd in x_d])
T4 = np.array([periodg4(xd) for xd in x_d])


plt.plot(x_d , T1)
plt.plot(x_d , T2)
plt.plot(x_d , T3)
plt.plot(x_d , T4)

plt.yscale("log")

plt.xlabel("$x_0$")
plt.ylabel("$T$")

plt.show()
