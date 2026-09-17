#Python Parte 15: Ereditarieta
#Oggi in questo video parleremo di ereditarieta
#Ereditarieta permette a una classe di riutilizzare attributi e metodi di un altra classe
#la classe da cui ereditiamo viene chiamata CLASSE PADRE
#la classe che eredita viene chiamata CLASSE FIGLIA
#Creiamo la classe Padre
class Animale:
    def mangia(self):
        print("Animale sta mangiando")
#Cane eredita da animale
class Cane(Animale):
    pass
#Creiamo un oggetto Cane
rex = Cane()
#Costruttore e ereditarieta
#Qui introduciamo gli attributi
class Animale:
    def __init__(self, nome):
        self.nome = nome
    def presenta(self):
        print("Mi chiamo", self.nome)
class Cane(Animale):
    def abbaia(self):
        print("Bau")
rex = Cane("Rex")
rex.presenta()
rex.abbaia()
#Riepilogo
#EREDITARIETA: Una classe puo ereditare caratteristiche da un altra classe
#CLASSE PADRE: fornisce attributi e metodi comuni
#CLASSE FIGLIA: eredita e puo aggiungere nuove funzionalita
