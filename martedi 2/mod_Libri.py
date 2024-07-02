class Libri:        #CLASSE LIBRI
    
    def __init__(self, ISBN):   #COSTRUTTORE
        self.isbn=ISBN
        self.titolo=input("Inserisci il titolo del libro: ")
        self.autore=input("Inserisci l'autore del libro: ")

    #RITORNA LA DESCRIZIONE DEL LIBRO
    def descrizione(self):
        return f"Il libro \"{self.titolo}\" è stato scritto da {self.autore}. Il suo codice ISBN è {self.isbn}"
    
    #RITORNA IL TITOLO DEL LIBRO
    def getTitolo(self):
        return self.titolo
    