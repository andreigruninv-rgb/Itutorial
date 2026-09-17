#Python Parte 14: Incapsulamento
#Oggi in questo video vi parlero di incapsulamento
#incapsulamento permette di controllare come i dati di un oggetto possono essere utilizzati
#e modificati
#1) ATTRIBUTI PUBBLICI
#Partiamo da un esempio molto semplice
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
#Creiamo un oggetto Persona
persona = Persona("Luca", 17)
#Possiamo accedere direttamente agli attributi
print(persona.nome) # Luca
print(persona.eta) # 17
#2) PERCHE SERVE INCAPSULAMENTO
#Immaginiamo di avere un conto bancario
class ContoBancario:
    def __init__(self, saldo):
        self.saldo = saldo
conto = ContoBancario(1000)
print(conto.saldo) # 1000
conto.saldo = -500
print(conto.saldo) # -500
#Abbiamo creato un problema
# un saldo bancario non dovrebbe poter diventare negativo semplicemente modificando un attributo
#Vorremmo invece controllare il valore prima di modificarlo
#3) ATTRIBUTI CON UN SOLO _
#questo indica che attributo dovrebbe essere considerato interno alla classe
class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo
conto = ContoBancario(1000)
print(conto._saldo) 
#ATTENZIONE! il singolo underscore NON rende veramente privato attributo
#4) ATTRIBTUI CON DUE _
#Possiamo utilizzare 2 underscore: __saldo
#Questa attiva il meccanismo chiamato NAME MANGLING
class ContoBancario:
    def __init__(self, saldo):
        self.__saldo=saldo
conto = ContoBancario(1000)
print(conto.__saldo) # Qui genera AttributeError
#5) GETTER
#Questo meccanismo serve per visualizzare un attributo al video quando e privato
class ContoBancario:
    def __init__(self, saldo):
        self.__saldo=saldo
    def get_saldo(self):
        return self.__saldo
conto = ContoBancario(1000)
print(conto.get_saldo()) # 1000
#6) SETTER
#Questo meccanismo permette di modificare attributo privato
class ContoBancario:
    def __init__(self, saldo):
        self.__saldo=saldo
    def set_saldo(self, nuovo_saldo):
        self.__saldo=nuovo_saldo
conto = ContoBancario(1000)
conto.set_saldo(78)
print(conto.get_saldo()) # 78
