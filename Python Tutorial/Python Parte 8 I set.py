#Python Parte 8: I set
#In questa lezione impariamo cosa sono i set
#e come utilizzarli in Python
#Un set e la collezione di elementi:
#non ordinata
#senza duplicati
#modificabile
#2) Creare il set
frutti = {"mela", "banana", "arancia"}
print(frutti) #{'mela', 'banana', 'arancia'}
#3) I Duplicati
numeri = {1, 2, 2, 3, 3, 3, 4}
print(numeri) #{1, 2, 3, 4}
#elimina dei duplicati
#I set eliminano automaticamente i duplicati
#Per creare set vuoto
#serve fare:
vuoto = set()
print(type(vuoto)) # <class 'set'>
#4) aggiungere gli elementi
frutti.add("papaya")
print(frutti)
#5) Se proviamo ad aggiungere elemento che gia esiste non viene duplicato
frutti.add("banana")
print(frutti)
#6) eliminare elemento
frutti.remove("papaya")
print(frutti)
#7) per eliminare un elemento che non esiste utilizzando remove ci sara un errore
# utilizziamo discard che e piu sicuro
frutti.discard("mango")
print(frutti)
#8) controllare se un elemento esiste
if "banana" in frutti:
    print("Questo elemento e presente nei set. ")
#9) Possiamo scorrere i set con ciclo for
for frutta in frutti:
    print(frutta)
#10) Unione: unisce i due set
a = {1, 2, 3}
b = {4, 5, 6}
unione = a | b
print(unione)
#11) Intersezione: prendono elementi in comune tra i due set
a = {1, 2, 3}
b = {3, 4, 5}
intersezione = a & b
print(intersezione)
#12) Differenza: otteniamo gli elementi presenti in A, ma non presenti in B
a = {1, 2, 3}
b = {3, 4, 5}
differenza = a - b
print(differenza)
#13) differenza simmetrica: prende elementi differenza tra 2 set
a = {1, 2, 3}
b = {3, 4, 5}
risultato = a ^ b
print(risultato)
# La differenza tra lista e set
#lista: mantiene i duplicati, mantiene ordine
#set: elmina i duplicati, non garantisce l'ordine