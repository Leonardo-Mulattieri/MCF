import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')

def massainvariante( E1, px1, py1, pz1 ,E2, px2, py2, pz2):
    E = E1 + E2
    px = px1 + px2
    py = py1 + py2
    pz = pz1 + pz2
      
    mc2 = np.sqrt((E)**2 - (px**2 + py**2 + pz**2))

    return mc2

k =  massainvariante(dataset['E1'],dataset['px1'],dataset['py1'],dataset['pz1'],dataset['E2'], dataset['px2'], dataset['py2'], dataset['pz2'])

"""
n,bins,p = plt.hist(k  , bins = 100, range = (np.min(k) ,np.max(k)), color = 'blue')

plt.show()
"""

n,bins,p = plt.hist(k  , bins = 100, range = (2.8 , 3.4) , color = 'gold')






from scipy import optimize

"""
A = h del picco
m ( media )  = pos. centro picco
sigma = larghezza del picco
"""

def fg1(x, A ,m, sigma, p1, p0 ):
    Gauss = A*np.e**(-((x-m)**2/(2*sigma**2)))
    # +
    Poli = p1*x + p0
    return Gauss + Poli

def fg2(x , A1 , A2 , m , sigma1 , sigma2 , p1 , p0):
    Gauss1 = A1*np.e**(-((x-m)**2/(2*sigma1**2)))
    # +
    Gauss2 = A2*np.e**(-((x-m)**2/(2*sigma2**2)))
    # +
    Poli = p1*x + p0
    return Gauss1 + Gauss2 + Poli


bin_c = 0.5* (bins[1:] + bins[:-1])

mask = (bin_c > 2.8) & (bin_c < 3.4)
x_fit = bin_c[mask]
y_fit = n[mask]

yerr = np.sqrt(n)
yerr_fit = yerr[mask]

#funzione 1
params, params_covariance = optimize.curve_fit(fg1 , x_fit , y_fit,sigma = yerr_fit, absolute_sigma = True,  p0 = [1000, 3.1, 0.03, 0.0, 100.0])

xtest = np.linspace(2.8, 3.4 , 100)

# *params mi "spacchetta" tutti e 5 i valori che mi servono nella funziona, simile a come funziona il terminale
ytest = fg1(xtest, *params)

plt.errorbar( xtest, ytest, yerr = yerr_fit,  color = 'limegreen')
plt.show()


yx2 = fg1(x_fit, *params)
chi2 = np.sum( (yx2 - ytest)**2 / y_fit)

ndof = len(x_fit) - len(params)

nomi = ['A', 'mu', 'sigma', 'p1', 'p0']
K2 = ['Chi2']

print("Funzione 1\n")
print(f"{'Parametro':<10}{'Valore':>14}")
print('-' * 55)
for nome, v in zip(nomi, params):
    print(f"{nome:<10}{v:>14f}")
print('-' * 55)

print(f"chi2      = {chi2:.2f}")


#funzione 2
params, params_covariance = optimize.curve_fit(fg2 , x_fit , y_fit,sigma = yerr_fit, absolute_sigma = True,  p0 = [1000, 2000,  3.1, 0.03, 0.08,  0.0, 100.0])


ytest2 = fg2(xtest , *params)

n,bins,p = plt.hist(k  , bins = 100, range = (2.8 , 3.4) , color = 'gold')
plt.errorbar( xtest, ytest2, yerr = yerr_fit,  color = 'red')
plt.show()

yx22 = fg2(x_fit, *params)
chi22 = np.sum( (yx22 - ytest2)**2 / y_fit)

ndof = len(x_fit) - len(params)

nomi = ['A1', 'A2' , 'mu', 'sigma1', 'sigma2', 'p1', 'p0']
K2 = ['Chi2']

print("Funzione 2\n")
print(f"{'Parametro':<10}{'Valore':>14}")
print('-' * 55)
for nome, v in zip(nomi, params):
    print(f"{nome:<10}{v:>14f}")
print('-' * 55)

print(f"chi2      = {chi22:.2f}")

#Funzione 1
# Grafico con Rapportp Dati/Fit

fig, ax = plt.subplots( 3, 1 , figsize = (9 , 6), gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True)
fig.subplots_adjust(hspace=0.05)

ax[0].set_title('Fit', fontsize=16, color='darkred')
ax[0].errorbar(x_fit,  y_fit,  yerr=yerr_fit, color='royalblue', fmt='o', label='Dati')
ax[0].plot( xtest, ytest,color='darkorange' ,label='Fit$')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].errorbar(x_fit,  y_fit - yx2,  yerr=yerr_fit, fmt='o', color='royalblue' )
ax[1].axhline(0, color='darkorange') 
ax[1].set_ylabel('Dati- Fit',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14)      
ax[1].grid(True, axis='y')

# Grafico subplot 2 (rapporto dati / funzione di fit / errore)
ax[2].errorbar(x_fit,  (y_fit - yx2)/yerr_fit,  yerr=yerr_fit**2/yx2, fmt='o', color='royalblue' )
ax[2].axhline(0, color='darkorange') 
ax[2].set_ylabel('(Dati - Fit)/err',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].grid(True, axis='y')

plt.show()

#funzione 2
# Grafico con Rapportp Dati/Fit

fig, ax = plt.subplots( 3, 1 , figsize = (9 , 6), gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True)
fig.subplots_adjust(hspace=0.05)

ax[0].set_title('Fit', fontsize=16, color='darkred')
ax[0].errorbar(x_fit,  y_fit,  yerr=yerr_fit, color='royalblue', fmt='o', label='Dati')
ax[0].plot( xtest, ytest2 ,color='darkorange' ,label='Fit$')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].errorbar(x_fit,  y_fit - yx22,  yerr=yerr_fit, fmt='o', color='royalblue' )
ax[1].axhline(0, color='darkorange') 
ax[1].set_ylabel('Dati- Fit',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14)      
ax[1].grid(True, axis='y')

# Grafico subplot 2 (rapporto dati / funzione di fit / errore)
ax[2].errorbar(x_fit,  (y_fit - yx22)/yerr_fit,  yerr=yerr_fit**2/yx2, fmt='o', color='royalblue' )
ax[2].axhline(0, color='darkorange') 
ax[2].set_ylabel('(Dati - Fit)/err',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].grid(True, axis='y')

plt.show()

