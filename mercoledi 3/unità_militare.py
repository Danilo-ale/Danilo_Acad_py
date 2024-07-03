from random import randint
class UnitaMilitare:
    counter_unita=0
    def __init__(self, nome, numero_soldati):
        UnitaMilitare.counter_unita+=1
        self.nome=nome
        self.numero_soldati=numero_soldati
        self.x=int(input("Inserisci la coordinata x attuale: "))
        self.y=int(input("Inserisci la coordinata y attuale: "))
        self.obb_x=0
        self.obb_y=0
    def muovi(self):
        nx=input("Inserisci la coordinata x in cui spostare l'unità: ")
        ny=input("Inserisci la coordinata y in cui spostare l'unità: ")
        """ if nx>self.x and ny>self.y:
            print("L'unità si sta muovendo a nord-est")
        elif nx>self.x and ny==self"""
        print(f"L'unità si sta muovendo da {self.x}.{self.y} a {nx}.{ny}")
        self.x=nx
        self.y=ny

    def attacca(self):
        self.obb_x=int(input("Indicare la coordinata x dell'obbiettivo: "))
        self.obb_y=int(input("Indicare la coordinata y dell'obbiettivo: "))
        #UTILIZZARE RANDINT PER VEDERE SE HA COLPITO O NO (1 colpito, 0 mancato)
        print(f"L'obbiettivo alle coordinate {self.obb_x}.{self.obb_y} è stato attaccato.")

    def ritira(self):
        if self.obb_x==0 and self.obb_y==0:
            print("Nessuna ritirata strategica. Unità in base.")
        else:
            print("Ritirata strategica in base.")
            self.x=0
            self.y=0

class Fanteria(UnitaMilitare):
    counter_fanteria=0
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        Fanteria.counter_fanteria+=1
    
    def costruisci_trincea(self):
        print("\nInserimento dati posizione trincea: ")
        nx=input("Inserisci la coordinata x: ")
        ny=input("Inserisci la coordinata y: ")
        print(f"Unità fanteria {self.nome} spostata da {self.x}.{self.y} a {nx}.{ny}")
        self.x=nx
        self.y=ny

    def getPosizione(self):
        return f"Posizione unità di fanteria \"{self.nome}\": {self.x}.{self.y}"
    

class ControlloMilitare(Fanteria):
    def __init__(self):
        self.registro={}
        self.registro["Fanteria"]=Fanteria.counter_fanteria
    
    def mostra_unita(self):
        for divisione in self.registro.keys():
            print(f"Divisione \"{divisione}\". Numero unità: {self.registro[divisione]}")


f1=Fanteria("Gino",50)
f1.costruisci_trincea()


print(f1.getPosizione())

contr1=ControlloMilitare()
contr1.mostra_unita()


