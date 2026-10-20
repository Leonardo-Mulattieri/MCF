g_s = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
g_o = g_s[3:7] + g_s* 3 + g_s[0:6]
print('\nI giorni di ottobre sono:', g_o)

n=[]
k = 0
for i in range(1,32):
 k = i
 n.append(k)

for a,b in zip(g_o,n):
  D_O = {a:b}

 print(D_O)
