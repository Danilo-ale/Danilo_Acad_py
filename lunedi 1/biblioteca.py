class Libri:
    autore=""
    titolo=""
    pagine=""
    def __init__(self, titolo,autore,pagine):
        self.autore=autore
        self.titolo=titolo
        self.pagine=pagine
    def __str__(self):      #
        return(f"Il libro \"{self.titolo}\" è stato scritto da {self.autore} e ha {self.pagine} pagine")

class Biblioteca:
    libreria=[]
    def CreaLibro(self):
        
        id=0
        while True:
            autore=input("Inserisci autore: ")
            titolo=input("Inserisci titolo: ")
            pagine=input("Inserisci numero di pagine: ")
            libro=Libri(autore,titolo,pagine)
            Biblioteca.libreria.append(libro)
            id+=1
            scelta=input("Continuare? ").lower()
            if scelta!="si":
                break
    def Visualizza(self):
        for libro in Biblioteca.libreria:
            print(libro)
    

biblio=Biblioteca()
biblio.CreaLibro()
biblio.Visualizza()      
