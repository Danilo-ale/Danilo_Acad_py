from math import sqrt

class Punti:
    x=0
    y=0
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def muovi(self, dx,dy):
        self.x=dx
        self.y=dy
    def distanza_0(self):
        self.distanza_0=sqrt(self.x**2+self.y**2)
        print("Distanza è:",self.distanza_0)
    def distanza(self, nuovax,nuovay):
        self.distanza=sqrt((self.x-nuovax)**2+(self.y-nuovay)**2)
        print("Distanza è:",self.distanza)
punto1=Punti(2,5)
print(punto1.x, punto1.y)
punto1.muovi(5,4)
print(punto1.x, punto1.y)
print("distanza da origine:")
punto1.distanza_0()
x,y=input("Inserisci due coordinate: ").split(" ")
punto1.distanza(int(x),int(y))


