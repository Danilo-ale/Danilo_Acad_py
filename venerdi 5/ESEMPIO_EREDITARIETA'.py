"""
EREDITARIETA': è una regola fondamentale dei linguaggi OOP. Permette di
creare una classe che eredita i vari metodi e attributi di una classe chiamata padre o superclasse
A differenza dell'incapsulamento, che serve a nascondere dei valori, l'ereditarietà 
permette di estenderli ad altri classi "figlie" 

Le caratteristiche principali di questa regola sono:
1. Possibilità di effettuare un over ride dei metodi della sclasse padre:
    la classe figlia può sovrascrivere i metodi della sua superclasse per
    estendere o modificare il comportamento, in modo da renderlo 
    compatibile con le caratteristiche della classe figlio
2. Metodo super(). Permette di accedere ai metodi della superclasse
    per permettere l'over-ride 

3. Ereditarietò multipla: a differenza di altri linguaggi OOP, Python
    permette ad una classe di essere figlio di più "padri", quindi
    ereditare attributi e metodi di più superclassi contemporaneamente
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