import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

#ci interessano principalmente E1 e px1 ?

DataSet_Gen = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')

dataset = DataSet_Gen[['E1','px1','py1','pz1','E2','px2','py2','pz2']] 

def massainvariante( E1, px1, py1, pz1 ,E2, px2, py2, pz2):
    E = E1 + E2
    px = px1 + px2
    py = py1 + py2
    pz = pz1 + pz2
      
    mc2 = np.sqrt((E)**2 - (px**2 + py**2 + pz**2))

    return mc2

k =  massainvariante(dataset['E1'],dataset['px1'],dataset['py1'],dataset['pz1'],dataset['E2'], dataset['px2'], dataset['py2'], dataset['pz2'])


n,bins,p = plt.hist(k  , bins = 100, range = (np.min(k) ,np.max(k)), color = 'blue')


"""
n,bins,p = plt.hist(k  , bins = 100, range = (2.8 , 3.4) , color = 'gold')
plt.show()

"""


from scipy import optimize

"""
A = h del picco
mu = pos. centro picco
sigma = larghezza del picco
m,q = ?
"""

def fg1(x, A ,mu, sigma, p1, p0 ):
    Gauss = A*np.e**(-((x-mu)**2/(2*sigma**2)))
    # +
    Poli = p1*x + p0
    return Gauss + Poli

bin_c = 0.5* (bins[1:] + bins[:-1])

mask = (bin_c > 2.95) & (bin_c < 3.25)
x_fit = bin_c[mask]
y_fit = n[mask]

yerr = np.sqrt(n)
yerr_fit = yerr[mask]

params, params_covariance = optimize.curve_fit(fg1 , x_fit , y_fit,sigma = yerr_fit, absolute_sigma = True,  p0 = [3000, 3.1, 0.03, 0.0, 50.0])

xtest = np.linspace(np.min(k), np.max(k), 1000)

# *params mi "spacchetta" tutti e 5 i valori che mi servono nella funziona, simile a come funziona il terminale
ytest = fg1(xtest, *params)



plt.errorbar( xtest, ytest,  color = 'limegreen')

plt.show()
