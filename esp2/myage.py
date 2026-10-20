from datetime import datetime, timedelta

data_str = input('Inserisci la tua data di nascit [Giorno-Mese-Anno Ora:Minuto:Secondo]:')


datenow = datetime.now()

data = datetime.strptime(data_str, "%d-%m-%Y %H:%M:%S")

timediff = datenow - data

timediff_a = datenow.year - data.year

timediff_s = timediff.total_seconds()

T_g = timediff_s/24/3600

D_def = 'ho {:} anni, in giorni ho {:} giorni e in secondi ho {:} secondi'.format(timediff_a, T_g, timediff_s)

#print(D_def)

A = float(timediff_a)
B = float(T_g)
C = float(timediff_s)
#print(type(A))

Tempo = [A , B , C]
Date_0 = ['Hai vissuto questi anni: ','Hai vissuto questi giorni in totale: ','Hai vissuto questi secondi in totale: ']



for i,j in zip(Date_0,Tempo):
  print('{:<10} {:20}'.format(i,j))
