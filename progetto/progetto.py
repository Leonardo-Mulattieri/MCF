import numpy as np
import sys
import os



class dati_av:

    def __init__(self, nome_oggetto, coord_ix , coord_iy , velocità_ix , velocità_iy , massa, gravità, coefficente_a, angolo):
        self.n = nome_oggetto
        self.x =coord_ix #posizione iniziale per le x
        self.y =coord_iy #posizione iniziale per le y
        self.v0x = velocità_ix #in m/s
        self.v0y = velocità_iy #in m/s
        self.m = massa #in kg
        self.g = gravità #in m/s^2
        self.k = coefficente_a 
        self.ang = angolo #tra vettore r e terra

    def vers(self):
        u_x = np.cos(self.ang)
        u_y = np.sin(self.ang)
        return u_x, u_y

    def ang_magg(self,other):
        return self.ang < other.ang

    def ang_min(self, other):
        return self.ang > other.ang



og1 = dati_av('bowling',0,0,0,0,0,0,0,10)
og2 = dati_av('calcio' ,0,0,0,0,0,0,0,100)
og3 = dati_av('medica', 0,0,0,0,0,0,0,0)



os.system('ls /usr');
