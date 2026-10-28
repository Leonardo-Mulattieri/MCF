import pandas as pd
import matplotlib.pyplot as plt


kepler = 'kplr010666592-2011240104155_slc.csv'
file_tot = pd.read_csv(kepler)
dati = file_tot[['TIME','TIMECORR','CADENCENO','SAP_FLUX','SAP_FLUX_ERR']]
#print("Colonne: ", dati.columns)

#minimo 950 - 952
"""
plt.errorbar(dati['TIME'],dati['SAP_FLUX'], xerr = dati['TIMECORR'], yerr = dati['SAP_FLUX_ERR'], fmt = 'o')
plt.xlabel('Tempo')
plt.ylabel('Flusso')
#plt.show()
"""
mind = dati.loc[ (dati['TIME'] > 950.) & (dati['TIME'] < 950.75)]
"""
plt.errorbar(mind['TIME'],mind['SAP_FLUX'],xerr =mind['TIMECORR'],yerr = mind['SAP_FLUX_ERR'], fmt = 'o')
plt.xlabel('Tempo')
plt.ylabel('Flusso')
#plt.show()
"""
fig, gt = plt.subplots(figsize=(12, 6))

gt.errorbar(dati['TIME'],dati['SAP_FLUX'],xerr = dati['TIMECORR'],yerr = dati['SAP_FLUX_ERR'], fmt = 'o')
gt.set_xlabel('Tempo')
gt.set_ylabel('Flusso')

gz = gt.inset_axes([0.75 , 0.75, 0.2 , 0.2])
gz.errorbar(mind['TIME'],mind['SAP_FLUX'],xerr =mind['TIMECORR'],yerr = mind['SAP_FLUX_ERR'], fmt = 'o')

plt.show()
