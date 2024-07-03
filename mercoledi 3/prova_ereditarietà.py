class Padre:
    def __init__(self,nome):
        self.nome=nome
    
class Padre2:
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome


class Figlio(Padre2,Padre):
    def __init__(self, nome, cognome):
        super().__init__(nome,cognome)



f1=Figlio("gino","postino")

print(f1.nome, f1.cognome)