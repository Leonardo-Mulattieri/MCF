import sys

sys.path.append('../../accessori/L05')

import somme

ns = input("inserisci un numero naturale: ")
es = input("inserisci la potenza della radice: ")
#as = input("inserisci la potenza a cui n verrà elevato: ")
#lo metto come commento per confermare che abbia messo a come valore di default = 1

n = int(ns)
e = int(es)
#a = int(as)

k1,k2 = somme.sum_prod(n)
j1,j2 = somme.rad_pow(n,e)

if __name__ == "__main__":
    print('Hai scelto {:}; la loro sommatoria è {:} e il loro prodotto è {:}'.format(n, k1, k2))
    print('Hai scelto {0} e potenze della radice {1}; la somme delle radice è allora {2} mentre la sommatoria di {0} alla potenza scelta è {3}'.format(n,e,j1,j2))
