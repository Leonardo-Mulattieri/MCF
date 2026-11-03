import pandas as pd
import numpy as np
import sys

sys.path.append('../../accessori/L05')

import progetto



g = 9.81

dati = pd.DataFrame( columns = ['oggetto','coord_x_0', 'coord_y_0','velocità_0x', 'velocità_0y','massa', 'gravità','coefficente attrito viscoso', 'angolo'])

nomi = np.array(['palla da bowling', 'palla medica'])
x_0 = np.array([0,0])
y_0 = np.array([0.20, 1.60])
v0x = np.array([ 5 , 0 ])
v0y = np.array([ 0 , 10])
m = np.array([2 , 8])
gr = np.array([g , g])
k = np.array([1 , 1])
ang = np.array([0, 60])


og1 = progetto.dati_av('bowling',0,0,0,0,0,0,0,10)
og2 = progetto.dati_av('calcio' ,0,0,0,0,0,0,0,100)
og3 = progetto.dati_av('medica', 0,0,0,0,0,0,0,0)



print(og1.ang_magg(og3))

#git add #nome_cartella_con_tutto_dentro/*.py
#git commit -a -m '#commento del file'
#git push
