#Python Parte 5: spiegazione completa delle variabili, type(), tipi di dati, casting
#oggi in questo video impariamo a:
#creare variabili
#conoscere i principali tipi di dati
#convertire i dati con il casting
#variabile str
nome="Marco"
print(nome) #"Marco"
print(type(nome)) #str
#variabile int
numero=25
print(numero) #25
print(type(numero)) #int
#variabile float
prezzo=7.50
print(prezzo) #7.50
print(type(prezzo)) #float
#variabile bool
risposta=True
print(risposta) #True
print(type(risposta)) #bool
#CASTING: e una funzione che permette di convertire i tipi della variabile
#casting str()
numero=25
print(str(numero)) #"25"
#casting int()
numero="25"
print(int(numero)) #25
#casting float()
numero="10.5"
print(float(numero)) #10.5
#casting bool
x = bool(1)
y = bool(0)
print(x) #True
print(y) #False
#CASTING si fa anche con input perche per esempio:
eta = input("Inserisci la tua eta: ")
print(type(eta)) #risulta str
#per questo bisogna convertire con int(), float()