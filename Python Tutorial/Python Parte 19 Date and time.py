#Python Parte 19: date and time
#In questo video vi parlero come si lavora con orario e data
#Importiamo il modulo datetime 
import datetime
#Data e ora attuali
now = datetime.datetime.now()
print(now)
#Solo la data
print(now.date())
#Solo orario
print(now.time())
#Creiamo una data personalizzata
data = datetime.date(2026, 12, 25)
print(data)
#Formattia,o la data
# %d = giorno
# %m = mese
# %Y = anno
print(now.strftime("%d/%m/%Y"))
#Data e ora formattate
# %H = ore
# %M = minuti
# %S = secondi
print(now.strftime("%d/%m/%Y %H:%M:%S"))
#Aggiungiamo un giorno
domani = now + datetime.timedelta(days=1)
print(domani)
#sottraiamo un giorno
ieri = now - datetime.timedelta(days=1)
print(ieri)
#Differenza tra 2 date
data1 = datetime.date(2026, 9, 15)
data2 = datetime.date(2026, 12, 25)
differenza = data1 - data2
print(differenza.days)
#Convertiamo una stringa in una data
testo = "25/12/2026"
data = datetime.datetime.strptime(testo, "%d/%m%/Y")
print(data)