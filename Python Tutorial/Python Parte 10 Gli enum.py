#Python Parte 10: Gli Enum
#In questa lezione vediamo gli ENUM
# Un enum permette di creare un insieme di valori
# con un nome preciso e facilmente ricnonoscibile
# e molto utile quando abbiamo numero limitato di valori possibili
#1) Importare ENUM
#per utilizzare ENUM dobbiamo mettere from enum import ENUM
from enum import Enum
class Giorno(Enum):
    LUNEDI = 1
    MARTEDI = 2
    MERCOLEDI = 3
    GIOVEDI = 4
    VENERDI = 5
    SABATO = 6
    DOMENICA = 7
#Ogni valore ha:
# - un nome
# - un valore associato
#2) UTILIZZARE ENUM
#Possiamo accedere a un elemento dell'Enum
#utilizzando il nome della classe
print(Giorno.LUNEDI) # LUNEDI
#Possiamo accedere al nome di elemento
print(Giorno.LUNEDI.name)
#Possiamo accedere al valore di elemento
print(Giorno.LUNEDI.value)
#3) CONFRONTARE I VALORI
giorno = Giorno.SABATO
if giorno == Giorno.SABATO:
    print("E sabato")
# ENUM E IF / ELIF
giorno = Giorno.DOMENICA
if giorno == Giorno.LUNEDI:
    print("E lunedi")
elif giorno == Giorno.SABATO:
    print("E sabato")
elif giorno == Giorno.DOMENICA:
    print("E Domenica")
#ENUM E MATCH
#Possiamo utilizzare Enum anche con match
#match e particolarmenre utile quando abbiamo diversi casi possibili
giorno = Giorno.VENERDI
match giorno:
    case Giorno.LUNEDI:
        print("E lunedi")
    case Giorno.MARTEDI:
            print("E martedi")
    case Giorno.MERCOLEDI:
            print("E mercoledi")
    case Giorno.GIOVEDI:
            print("E giovedi")
    case Giorno.VENERDI:
            print("E venerdi")
    case Giorno.SABATO:
            print("E sabato")
    case Giorno.DOMENICA:
            print("E domenica")
#SCORRERE UN ENUM
#Possiamo socrrere utilizzando un for
for giorno in Giorno:
    print(giorno.name, giorno.value) # ogni elemento contiene nome e valore associato
#PERCHE UTILIZZARE ENUM
#Gli Enum rendono il codice:
# - piu leggibile
# - piu organizzato
# - piu facile da mantenere
# - meno soggetto a valori
#FINE LEZIONE