PRIMONUMERO = input('metti due valori interi, prima mettine uno, poi va a capo:')
SECONDONUMERO = input('')
i = int(PRIMONUMERO)
j = int(SECONDONUMERO)
print('In rappresentazione binaria: ',bin(i), ', ', bin(j))
print('\nIn rappresentazione esadecimale: ', hex(i), ', ', hex(j))


print("\n\nRisultato in rappresentazione binaria dell'operazione OR tra i 2 numeri scelti (a|b) : {:06b}".format(i|j))
print("\nRisultato in rappresentazione binaria dell'operazione AND tra i 2 numeri scelti (a&b) : {:06b}".format(i&j))
print("\nRisultato in rappresentazione esadecimale dell'operazione OR tra i 2 numeri scelti (a|b) : {:06x}".format(i|j))
print("Risultato in rappresentazione esadecimale dell'operazione AND tra i 2 numeri scelti (a&b) : {:06x}".format(i|j))
