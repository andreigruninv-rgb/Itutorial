#Python Parte 2 Condizioni e Cicli
#In questo video vi parlero delle condizioni e Cicli
#La condizione if permette al programma
#di eseguire un istruzione quando una condizione e vera
#acquisisco numero da tastiera
numero = int(input("Inserisci numero intero: "))
if numero > 0:
    #permette di verificare se il numero e positivo
    print("E positivo")
else:
    if numero < 0:
        #numero non e negativo se non e positivo
        print("E negativo")
    else:
        #se nessuna dei 2 condizioni e vera 
        print("E zero")

#Ciclo FOR permette di ripetere 
#un istruzione per un determinato numero di volte
print("Numeri da 1 a 5")
for i in range(1,6):
    #permette di visualizzare i numeri da 1 a 5
    print(i)
#il ciclo WHILE continua a ripetere
#finche la condizione e vera
numero=1
print("Stampa numero fino a 5 finche la condizione e vera:")
while numero<=5:
    #stampiamo il valore della variabile
    print(numero)
    numero+=1