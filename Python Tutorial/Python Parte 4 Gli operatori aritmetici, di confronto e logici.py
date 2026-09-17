#Python Parte 4: Gli operatori
#In questo video vi spiego come si utilizzano gli operatori per 
#eseguire gli operazioni e confrontare i valori
#1 GLI OPERATORI ARITMETICI
a = 5
b = 8
print(a + b) # somma
print(a - b) # differenza
print(a * b) # prodotto
print(a / b) # divisione
#1.1 ALTRI OPERATORI ARITMETICI
print(a // b) # divisione intera
print(a % b) # resto della divisione
print(a ** b) # potenza
#2 OPERATORI DI CONFRONTO
a = 10
b = 5
print(a > b) # True
print(a < b) # False
print(a == b) # False
#SIGNIFICATO DI OGNI OPERATORE
# > maggiore
# < minore
# == uguale
# != diverso
# >= maggiore o uguale
# <= minore o uguale
#ATTENZIONE A = E ==
# = serve a assegnare il valore
x = 10
# == serve a confrontare i valori
print(x == 10)
#OPERATORI LOGICI
#and entrambe le condizioni devono essere True
eta = 18
print(eta >= 18 and eta <= 30)
#or basta una condizione True
giorno = "sabato"
print(giorno=="sabato" or giorno =="domenica")
#not nega il risultato
piove = True
print(not piove)