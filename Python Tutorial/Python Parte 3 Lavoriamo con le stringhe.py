#Python Parte 3 Lavorare con le stringhe
#metodi: upper(),lower(),capitalize(), title(), strip(), replace(), find()
#count(), startswith(), endswith(), isdigit(), isalpha(), split(), join()
#In questo video spieghero delle stringhe e a cosa servono
#per prima cosa le stringhe e un testo o il carattere
#upper() si usa per trasformare la stringa in maiuscolo
stringa="Ciao Mondo"
print(stringa.upper())
#lower() si usa per trasformare tutto in minuscolo
print(stringa.lower())
#capitalize() permette di trasfromare la lettera maiuscolo inizio della stringa
print(stringa.capitalize())
#title() permette di trasformare in ogni parola la lettera maiuscola iniziale
print(stringa.title())
#strip() elimina gli spazi sia a destra che a sinistra
print(stringa.strip())
#replace() sostituisce la parola della stringa in un altra
print(stringa.replace("Mondo", "Xondo"))
#find() permette di ricercare la stringa
print(stringa.find("Mondo"))
#count() conta le occorenze di un carattere della stringa
print(stringa.count("o"))
#startswith() permette di cercare il carattere che inizia
print(stringa.startswith("C"))
#endswith() permette di cercare il carattere che finisce
print(stringa.endswith("o"))
#isdigit() permette di sapere se quel carattere e numerico
print(stringa.isdigit())
#isalpha() permette di sapere se quel carattere e' numerico e alfabetico
print(stringa.isalpha())
#split() permette di trasformare la lista in stringhe
lista = "Ciao Mondo"
testo = lista.split(' ')
print(testo)
#join() permette di trasformare la lista in stringhe
lista = ["Ciao", "Mondo"]
testo = " ".join(lista)
print(testo)