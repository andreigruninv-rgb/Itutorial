#Python Parte 16: Funzioni
#Oggi in questo video vi parlero delle funzioni
#Una funzione e un blocco di codice che possiamo riutilizzare
#ogni volta che ne abbiamo bisogno
def saluta():
    print("Ciao Benevnuto nel mio programma")
#Per eseguiremla funzione dobbiamo chiamarla
saluta()
#Possiamo anche passare dei dati alla funzione attraverso ai parametri
def saluta(nome):
    print("Ciao", nome)  # import numpy as np
saluta("Andrei")
#Una funzione puo anche restituire il risultatio utilizzando la parola chiave return
def somma(a, b):
    return a + b
risultato = somma(5, 3)
print(risultato)
#In questo modo possiamo riutilizzare la stessa funzione con valori diversi
print(somma(10, 20))
print(somma(7, 4))
print(somma(100, 50))
#Concetto chiave: 
#Le funzioni ci permettono di:
#1 di evitare di ripetere lo stesso codice
#2 organizzare meglio il programma
#3 rendere il codice piu leggibile
#4 riutilizzare facilmente le nostre istruzioni
