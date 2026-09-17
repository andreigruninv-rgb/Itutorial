#Python Parte 11: test Unitari
#I test unitari servono per verificare che singole funzioni del nostro programma producano il risultato corretto
#Python mette a disposizione il modulo unittest
#per creare ed eseguire test automatici
#1) FUNZIONE DA TESTARE
def somma(a, b):
    return a + b
def moltiplica(a, b):
    return a * b
def is_pari(numero):
    return numero % 2 == 0
#2) CREAZIONE DEI TEST
import unittest
class TestFunzioni(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)
    def test_moltiplica(self):
        self.assertEqual(moltiplica(2, 3), 6)
    def test_numero_pari(self):
        self.assertTrue(is_pari(10))
    def test_numero_dispari(self):
        self.assertFalse(is_pari(7))
#3) AVVIO DEL TEST
if __name__ == "__main__":
    #Avvia automaticamente tutti i metodi
    #che inizia con 'test__'
    unittest.main()