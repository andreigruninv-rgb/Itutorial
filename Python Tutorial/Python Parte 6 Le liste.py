#Python Parte 6: Liste
#Come creare, modificare e utilizzare le liste in Python
#Creazione della lista
lista = ["mela", "banana", "arancia"]
#Visualizzazione degli elementi
print(lista) #['mela', 'banana', 'arancia']
#Visualizzazione di un elemento tramite indice
print(lista[0]) # mela
#Modificare un elemento
lista[0] = "papaya"
print(lista) #['papaya', 'banana', 'arancia']
#aggiungere un elemento tramite append()
lista.append("pera")
print(lista) #['papaya', 'banana', 'arancia', 'pera']
#inserire un elemento tramite insert()
lista.insert(2, "frutta del drago")
print(lista) #['papaya', 'frutta del drago', 'banana', 'arancia, 'pera']
#eliminare un elemento tramite indice pop()
lista.pop(3)
print(lista) #['papaya', 'frutta del drago', 'banana', 'pera']
#eliminare un elemento tramite remove()
lista.remove("papaya")
print(lista) #['frutta del drago', 'banana', 'pera']
#visualizzare un indice dove si trova un elemento tramite index()
indice = lista.index("frutta del drago")
print(indice)
#visualizzare la lista tramite for
for x in lista:
    print(x)
#cancellare tutta la lista tramite clear()
lista.clear()
print(lista) #[]
#ordinamento della lista tramite sort()
lista.sort()
print(lista)
#inversione degli elementi tramite reverse()
lista.reverse()
print(lista)
#come si unisce una o piu lista in uno solo tramite la join
lista2 = [4, 3, 5, 6]
lista3 = lista + lista2
print(lista3)
