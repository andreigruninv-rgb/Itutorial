#Python Parte 13: Programmazione orientato agli oggetti (OOP)
#Oggi vediamo uno dei concetti piu importanti di Python:
#La programmazione orientato agli oggetti chiamata anche OOP
#1) CREIAMO LA NOSTRA PRIMA CLASSE
#La classe e come un modello. Possiamo usarla per creare tanti oggetti dello stesso tipo
class Persona:
    pass
#ora possiamo creare un oggetto partendo dalla classe Persona
persona1 = Persona()
#persona1 e un istanza, cioe un oggetto della classe Persona
print(persona1)
#2) IL METODO __init__
#Solitamente vogliamo che ogni Persona abbia dei dati:
#Per esempio:
# - nome
# - eta
#Per inizializziare questi dati utilizziamo __init__
class Persona:
    #__init__ viene eseguito automaticamente ogni volta che creiamo un nuovo oggetto
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
#adesso creiamo degli oggetti
persona2 = Persona("Luca", 18)
persona3 = Persona("Marco", 23)
print(persona2.eta) # 18
print(persona3.nome) # Marco
# CHE COSA SIGNIFICA self
#quando scriviamo: self.nome
#stiamo dicendo: il nome appartiene a questo oggetto
#quindi: persona1.nome = Mario
#persona2.nome = Anna
#4) CREIAMO UN METODO
#Una classe non deve contenere solamente dati. Puo anche contenere funzioni
#Quando una funzione si trova dentro una classe
#viene chiamata METODO
class Persona: 
    def __init__(self, nome, eta):
            self.nome = nome
            self.eta = eta
    def presentarsi(self):
        print("Ciao sono", self.nome, "ho", self.eta)
persona3 = Persona("Marco", 23)
persona3.presentarsi()
#5) POSSIAMO MODIFICARE GLI ATTRIBUTI
persona3.nome = "Anna"
print(persona3.nome) # Anna
#RIEPILOGO
#Classe: e il modello utilizzato per creare gli oggetti
#Oggetto: un istanza della classe
#attributi: e un dato appartenente a un oggetto
#metodo: e una funzione appartenente alla classe
#__init__: serve a inizializzare un nuovo oggetto
#self: rappresenta istanza corrente