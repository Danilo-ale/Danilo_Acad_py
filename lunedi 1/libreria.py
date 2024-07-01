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
    

libro1=Libri("Windows","Bill Gates", 120)
libro2=Libri("Titolo","Autore","pagine")
#libro1.__str__()

libreria=[]
libreria.append(libro1)
libreria.append(libro2)
#print(libro1)
for libro in libreria:
    print(libro)