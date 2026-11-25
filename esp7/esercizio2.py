import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2026/refs/heads/main/dati/integrazione_derivazione/oscilloscope.csv'
dataset = pd.read_csv(url)
print(dataset.head())

#per trasformare le colonne in array
t = dataset['time'].values
s1 = dataset['signal1'].values
s2 = dataset['signal2'].values


fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
ax[0].plot(t, s1, color='royalblue')
ax[0].set_ylabel('Segnale 1')
ax[1].plot(t, s2, color='darkorange')
ax[1].set_ylabel('Segnale 2')
ax[1].set_xlabel('Tempo')
ax[0].set_title('Segnali dell\'oscilloscopio')


# f'(x_i) ~ (f(x_{i+h}) - f(x_{i-h})) / (x_{i+h} - x_{i-h})
# h = numero di punti di distanza dal punto centrale
def derivata_centrale(x, y, h):
    dy = y[2*h:] - y[:-2*h]
    dx = x[2*h:] - x[:-2*h]
    return x[h:-h], dy / dx


valori_h = [1, 5, 20]
colori = ['lightgray', 'royalblue', 'red']

fig, ax = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
for h, c in zip(valori_h, colori):
    x1, d1 = derivata_centrale(t, s1, h)
    x2, d2 = derivata_centrale(t, s2, h)
    ax[0].plot(x1, d1, color=c, label=f'h = {h}')
    ax[1].plot(x2, d2, color=c, label=f'h = {h}')

ax[0].set_ylabel('Derivata segnale 1')
ax[1].set_ylabel('Derivata segnale 2')
ax[1].set_xlabel('Tempo')
ax[0].set_title('Derivata (differenza centrale)')
ax[0].legend()
ax[1].legend()

i1 = np.argmin(s1)
i2 = np.argmin(s2)
print(f'Segnale 1: minimo = {s1[i1]:.2f} a t = {t[i1]}')
print(f'Segnale 2: minimo = {s2[i2]:.2f} a t = {t[i2]}')

plt.show()
