#Python Parte 9: Dizionario
#Un dizionario permette di memorizzare i dati
#utilizzando una coppia: chiave -> valore
#1) CREARE IL DIZIONARIO
persona = {
    "nome":"Luca",
    "eta":20,
    "citta":"Roma"
}
print(persona) #{'nome':'Luca', 'eta':20, 'citta':'Roma'}
#2) ACCEDERE A UN VALORE
print(persona["nome"]) # Luca
print(persona["eta"]) # 20
#3) AGGIUNGERE UN ELEMENTO
#possiamo aggiungere una nuova coppia
#chiave -> valore
persona["professione"] = "Programmatore"
print(persona) #{'nome':'Luca', 'eta':20, 'citta':'Roma', 'professione':'Programmatore'}
#4) MODIFICARE IL VALORE
#Basta utilizzare una chiave gia esistente
persona["eta"] = 21
print(persona["eta"]) # 21
#5) ELIMINARE UN ELEMENTO
#Basta utilizzare metodo pop()
persona.pop("citta")
print(persona) #{'nome':'Luca', 'eta':20, 'professione':'Programmatore'}
#6) CONTROLLARE SE ESISTE UNA CHIAVE
if "nome" in persona:
    print("La chiave esiste!")
#7) CICLO FOR
# per visualizzare solo le chiavi
for chiave in persona:
    print(chiave) # nome, eta, professione
#Per visualizzare sia chiave che valori
for chiave, valore in persona.items():
    print(chiave, ":", valore)
#8) KEYS AND VALUES
#keys() -> si utilizza per visualizzare tutte le chiavi
print(persona.keys())
#values() - si utilizza per visualizzare solo le valori
print(persona.values())
