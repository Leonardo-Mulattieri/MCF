import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_tot = pd.read_csv('ExoplanetsPars_2025.csv', comment = '#')
dati = file_tot[['pl_orbper','pl_bmassj','pl_orbsmax','st_mass','discoverymethod']]

#print(dati.columns)

ssol = pd.DataFrame({
    'pl_name':    ['Mercurio', 'Venere', 'Terra', 'Marte','Giove', 'Saturno', 'Urano', 'Nettuno'],
    'pl_orbper':  [87.9, 224.7, 365.2, 686.9, 4332.5, 10759.2, 30688.5, 60182.0],
    'pl_bmassj':  [1.74e-4, 2.56e-3, 3.15e-3, 3.38e-4, 1.0, 0.2994, 0.0457, 0.0540],
    'pl_orbsmax': [0.387, 0.723, 1.0, 1.524, 5.204, 9.582, 19.201, 30.047],            
    'st_mass':    [1.0] * 8,                                 
})

"""
plt.scatter(dati['pl_orbper'],dati['pl_bmassj'] , color = 'green')
plt.scatter(ssol['pl_orbper'], ssol['pl_bmassj'], color = 'black')
plt.xlabel('Orbital Period', fontsize = 10)
plt.ylabel('Planet Mass',fontsize = 10)
plt.xscale('log')
plt.yscale('log')
plt.show()
"""

"""
plt.scatter(dati['pl_orbper'], (dati['pl_orbsmax']) ** 2 / dati['st_mass'] , color ='green')
plt.scatter(ssol['pl_orbper'], (ssol['pl_orbsmax']) ** 2 / ssol['st_mass'], color = 'black')
plt.ylabel('$R^2_{max} /m$', fontsize = 10)
plt.xlabel('Orbital Period',fontsize = 10)
plt.xscale('log')
plt.yscale('log')
plt.show()
"""


tr = dati.loc[(dati['discoverymethod'] == 'Transit')]
rv = dati.loc[(dati['discoverymethod'] == 'Radial Velocity')]

"""                                    
plt.scatter(tr['pl_orbper'], tr['pl_bmassj'], color = 'blue', alpha = 0.3, label = 'Transit')
plt.scatter(rv['pl_orbper'], rv['pl_bmassj'], color = 'red', alpha = 0.3, label = 'Radial Velocity')
plt.scatter(ssol['pl_orbper'], ssol['pl_bmassj'], color = 'black', alpha = 0.3, label = 'Sistema solare')
plt.legend(fontsize = 8)
plt.ylabel('Planet mass', fontsize = 10)
plt.xlabel('Orbital Period',fontsize = 10)
plt.xscale('log')
plt.yscale('log')
plt.show()
"""

maxx = max(tr['pl_bmassj'].max(), rv['pl_bmassj'].max(), ssol['pl_bmassj'].max())

"""

n, bins, p = plt.hist(tr['pl_bmassj'], bins=100, range = (0,maxx) ,color='gold' ,  alpha=0.3,  label = 'Transit' )
n, bins, p = plt.hist( rv['pl_bmassj'], bins=100,range = (0,maxx) , color='green',  alpha=0.3,label = 'Radial Velocity')
n, bins, p = plt.hist(ssol['pl_bmassj'], bins=100 ,range = (0, maxx) , color='blue', alpha=0.3,label = 'Solar system' )                
plt.legend(fontsize = 8)
plt.show()                                                                      """                                                      


lg_tv = np.log10(tr['pl_bmassj'])
lg_rv = np.log10(rv['pl_bmassj'])
lg_ssol = np.log10(ssol['pl_bmassj'])

max_log = max(lg_tv.max(), lg_rv.max(), lg_ssol.max())
min_log = min(lg_tv.min(), lg_rv.min(), lg_ssol.min())

n, bins, p = plt.hist(lg_tv, bins=100, range = (min_log,max_log) ,color='gold' ,  alpha=0.3,  label = 'Transit' )
n, bins, p = plt.hist( lg_rv, bins=100,range = (min_log,max_log) , color='green',  alpha=0.3,label = 'Radial Velocity')
n, bins, p = plt.hist(lg_ssol, bins=100 ,range = (min_log, max_log) , color='blue', alpha=0.3,label = 'Solar system' )               
plt.legend(fontsize = 8)
plt.show()                


"""
if np.log10(12032) != np.log(12032):
   print('o')
"""
