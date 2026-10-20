INTERO = input("inserisci un valore intero: ")
BIT = input("Inserisci il numero di bit a cui applicare lo shift: ")
i = int(INTERO)
t = int(BIT)

print("Rappresentazione binaria del numero intero: {:06b}".format(i))
print("Rappresentazione esadecimale del numero intero: {:06x}".format(i))


i_pt = ( i << t )
i_mt = ( i >> t )
print("spostanto {:} in rappresentazione binario di {:} bit a destra {:>1}".format(i,t, bin(i_pt)))
print("spostanto {:} in rappresentazione binario di {:} bit a sinistra {:>1}".format(i,t,bin(i_mt)))
