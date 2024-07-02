import mod_Libri
class Libreria:
    def __init__(self, nome):       #COSTRUTTORE
        self.lista_isbn=[]
        self.lista=[]
        self.nome=nome
    
    def getNome(self):      #getter nome libreria
        return self.nome

    def aggiungi_libro(self):       #METODO AGGIUNGI LIBRI
        while True:
            isbn=input("Inserisci l'ISBN del nuovo libro: ")
            if isbn not in self.lista_isbn:
                libro=mod_Libri.Libri(isbn)
                break
            else:
                print("codice ISBN già presente")
        self.lista.append(libro)
        self.lista_isbn.append(isbn)
        #print(libro)
        #print("Lista isbn", self.lista_isbn)
         #for isbn in self.lista_isbn:
          #  print(self.lista[self.lista_isbn.index(isbn)].descrizione())
    
    def rimuovi_libro(self,isbn_r): 
        trovato=False
        for isbn in self.lista_isbn:
            if isbn==isbn_r:
                self.lista.remove(self.lista[self.lista_isbn.index(isbn)])
                self.lista_isbn.remove(isbn)
                trovato=True
        if trovato:
            print("LIBRO ELIMINATO")
        else:
            print("LIBRO NON PRESENTE IN LISTA")

    #FUNZIONE CERCA PER TITOLO
    def cerca_per_titolo(self,titolo):
        trovato=False
        for libro in self.lista:    #CERCA NELLA LISTA DEGLI OGGETTI
            if titolo==libro.getTitolo():       #SE il titolo è presente nella lista degli oggetti
                print(libro.descrizione())      #...lo stampa
                trovato=True
        if trovato==False:
            print("libro non trovato")

    #FUNZIONA CHE PRINTA LA DESCRIZIONE DEL LIBRO
    def mostra_catalogo(self):
        x=1
        for libro in self.lista:
            print(f"{x}. {libro.descrizione()}")
            x+=1
