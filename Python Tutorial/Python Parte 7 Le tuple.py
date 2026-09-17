#Python Parte 7: Le Tuple
#La tupla e una raccolta dei valori
#E simile a una lista, ma NON puo essere modificata
#dopo essere stata creata
frutti = ("mela", "banana", "arancia")
print(frutti)
#Accedere agli elementi
frutti = ("mela", "banana", "arancia")
#Gli indici iniziano sempre a 0
print(frutti[0]) # mela
print(frutti[-1]) # arancia
#lunghezza della tupla
lunghezza = len(frutti)
print("lunghezza:", lunghezza)
#ATTENZIONE!
#La virgola e fondamentale
numeri=(10,)
print(type(numeri)) # '<class 'tuple'>'
numeri=(10)
print(type(numeri)) # <class 'int'>
#Scorrere una tupla con il ciclo
for frutta in frutti:
    print(frutta)
#Tuple e unpacking
#possiamo assegnare gli elementi
#della tupla a diverse variabili
persona = ("Luca", 25, "Italia")
nome, eta, nazione = persona
print(nome)
print(eta)
print(nazione)
#La differenza tralista e tupla e che:
#lista e modificabile
#invece tupla non e modificabile