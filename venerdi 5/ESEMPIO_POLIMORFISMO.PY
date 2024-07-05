"""
POLIMORFISMO: è la capacità di un oggetto cambiare forma ma non comportamento.
E' possibile attraverso l'over-riding dei metodi e permette ad oggetti
di classi diverse di essere considerati come oggetti di una classe comune.
Un esempio di polimorfismo è l'utilizzo della funzione len(), che può
essere applicata per indicare, per esempio, la lunghezza di una stringa
ma anche di una lista o dizionario.
"""

class Animale:
    def __init__(self, nome, età):
        self.nome = nome
        self.età=età

    def emetti_suono(self):
        print("Emetti suono")

class Cane(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)

    def emetti_suono(self):
        return "BAU"

class Gatto(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)

    def emetti_suono(self):
        return "MIAO"


cane=Cane("pippo",10)
gatto=Gatto("gianni",8)
print(cane.emetti_suono())
print(gatto.emetti_suono())