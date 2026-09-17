#Python Parte 20: Advanced Data Types
#1) Boolean
#True o False: utili per controllare condizioni
age = 20
print(age >= 18) # True
#2) None
#None significa "nessun valore"
user=None
print(user) # None
#3) Bytes
#Dati formato in binario
data = b"Python"
print(data)
#4) Bytearray
#Come bytes, ma modificabile
data = bytearray(b"Python")
data[0] = 74
print(data) # b'Python'
#5) Memoryview
#Permette di alvorare direttamente sui dati di memoria
data = bytearray(b"Python")
view = memoryview(data)
view[0] = 74
print(data) # b'Python'
#6) Frozenset
#Come un set, ma non modificabile
colors = frozenset(["red", "green", "blue"])
print(colors)
#7) Namedtuple
#Una tupla con nomi per i suoi elementi
from collections import namedtuple
Person = namedtuple("Person", ["name", "eta"])
person = Person("Luca", 25)
print(person.name) # Luca
print(person.eta) # 25
#8) OrderedDict
#Dizionario che mantiene ordine degli elementi
from collections import OrderedDict
users = OrderedDict()
users["luca"] = 25
users["Anna"] = 30
print(users)
#9) Counter
#Conta quante volte compare ogni elemento
from collections import Counter
words = ["python", "java", "python", "python"]
counter = Counter(words)
print(counter) # python : 3, java: 1
print(counter["python"]) # Python : 3
#10) Ellipsis
#Puo essere usato come segnaposto
def my_function():
    ...
print("Programma Terminato")