#Python Parte 18: Itertools
#Itertools e un modulo di Python che contiene strumenti utili
#per lavorare in modo semplice ed efficiente con gli iteratori
#Prima di tutto:
from itertools import count, cycle, repeat, chain, combinations, permutations, product
#count():
#genera una sequenza di numeri senza fine
for numero in count(1):
    print(numero)
    if numero == 5:
        break
#cycle()
#ripete continuamente gli elementi di una sequenza
colori = cycle(["rosso", "verde", "blu"])
for _ in range(5):
    print(next(colori))
#chain()
#unisce piu sequenza in un unico iteratore
numeri1 = [1, 2, 3]
numeri2 = [4, 5, 6]
tutti = chain(numeri1, numeri2)
print(list(tutti))
#combinations()
#crea tutte le possibili combinazioni possibili senza ripetere gli elementi
numeri = [1, 2, 3]
print(list(combinations(numeri, 2)))
#permutations()
#crea tutte le possibili permutazioni degli elementi
lettere = ["A", "B", "C"]
print(list(permutations(lettere, 2)))
#product()
#crea tutte le combinazioni possibili tra piu sequenze
colori = ["rosso", "blu"]
taglia = ["S", "M"]
print(list(product(colori, taglia)))
#In sintesi:
#itertools e molto utile quando dobbiamo creare sequenze, 
#combinazioni, permutazioni, o cicli, senza scrivere manualmente
#tanti for e senza creare inutilmente grandi strutture in memoria