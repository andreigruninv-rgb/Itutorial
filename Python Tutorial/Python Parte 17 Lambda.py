#Python Parte 17: Lambda
#Una lambda e una funzione anonima, cioe una funzione senza nome, utile 
#per operazioni semplici e veloci
#Sintassi:
#lambda argomenti: espressione
#Esempio
#Lambda con un argomento
quadrato = lambda x: x ** 2
print(quadrato(8)) # 64
#Lambda con piu di un argomento
somma = lambda a, b: a + b
print(somma(5, 2)) # 7
#Lambda con una condizione
pari = lambda x: x % 2 == 0
print(pari(8)) # True
#Lambda con map()
numeri = [1, 2, 3, 4]
doppi = list(map(lambda x: x * 2, numeri))
print(doppi) # [2, 4, 6, 8]
#Lambda con filter()
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari) #[2, 4]
#Lambda con sorted()
persone = [("Luca", 30), ("Anna", 20), ("Marco", 25)]
ordinate = sorted(persone, key=lambda persona:persona[1])
print(ordinate)
#In sintesi:
#lambda e ideale per funzioni brevi e semplici
#per funzioni piu complessi e meglio utilizzare def()