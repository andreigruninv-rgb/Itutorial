#Python Parte 12: Exception Handling
#COSE EXCEPTION
#Un eccezione e un errore che si verifica durante esecuzione del programma
#Python Interrompe il programma e genera: ZeroDivisionError
#TRY / EXCEPT
#con try possiamo eseguire un operazione che potrebbe generare un errore
try:
    numero = int(input("Inserisci un numero: "))
    risultato = 100 / numero
    print(risultato)
except ZeroDivisionError:
    #Se si verifica un errore, eseguiamo questo codice
    print("Qualcosa e andato storto")
#GESTIRE UN ECCEZIONE SPECIFICA
try:
    numero = int(input("Inserisci un numero: "))
    risultato = 100 / numero
except ValueError:
    #L utente non ha inserito un numero valido
    print("Devi inserire un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero. ")
#ELSE
#else viene eseguito solamente se NON si verifica nessuna eccezione
try:
    numero = int(input("Inserisci un numero: "))
    risultato = 100 / numero
except ValueError:
    #L utente non ha inserito un numero valido
    print("Devi inserire un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero. ")
else:
    print("Risultato:", risultato)
#FINALLY
#finally verra eseguito sempre, indipendemente dal risultato del try
try:
    numero = int(input("Inserisci un numero: "))
    risultato = 100 / numero
except ValueError:
    #L utente non ha inserito un numero valido
    print("Devi inserire un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero. ")
else:
    print("Risultato:", risultato)
finally:
    print("Operazione terminata")
#LEGGERE IL MESSAGGIO DELL ERRORE
try:
    numero = int("Ciao")
except ValueError as e:
    print("Errore:", e)
#RAISE
#con raise possiamo generare manualmente un eccezione
eta = 5
if eta < 0:
    raise ValueError("Eta non puo essere negativa")
#RIEPILOGO
#try -> codice potrebbe generare un errore
#except -> gestisce errore
#else -> eseguito se non ci sono errori
#finally -> eseguito comunque
#raise -> genera manualmente un eccezione
#Exception Handling = programmi piu robusti