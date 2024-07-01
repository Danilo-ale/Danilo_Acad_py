#classe ristoranti
class Ristoranti:           
    nome=""
    tipo_cucina=""
    def __init__(self, nome,tipo_cucina):       #costruttore
        self.menu={}
        self.nome=nome
        self.tipo_cucina=tipo_cucina
        self.aperto=False
    def descrivi_ristorante(self):  #funzione descrivi
        print(f"Benvenuto al ristorante \"{self.nome}\". Il suo tipo di cucina è \"{self.tipo_cucina}\"")

    def stato_apertura(self):
        if self.aperto==False:
            print("chiuso")     #print di ristorante chiuso o aperto
        else:
            print("aperto")
            
    def apri_ristorante(self):  #funzione apertura ristorante
        self.aperto=True
    def chiudi_ristorante(self):    #funzione chiusura ristorante
        self.aperto=False
    
    def aggiungi_al_menu(self,piatto,costo):        #funzione aggiungi piatto al menù
        if piatto not in self.menu.keys():  #verifica che non sia già presente nel menu
            self.menu[piatto]=costo
        else:
            print("Piatto già presente!")       #se è già presente, visualizza un messaggio di errore

    def togli_dal_menu(self,piatto):        #funzione elimina piatto dal menù
        if piatto in self.menu.keys():      #verifica che non sia già presente nel menu
            del self.menu[piatto]       #rimozione piatto dal dizionario
        else:
            print("Piatto non presente")

    def stampa_menu(self):
        if len(self.menu)>0:        #verifica che ci sia effettivamente almeno un piatto nel dizionario
            print("\nPiatti presenti:")
            for piatto in self.menu.keys():
                print(f"{piatto}, costo: {self.menu[piatto]}")  #visualizzazione nome e costo di ciascun piatto 
        else:
            print("Menù vuoto!")

            
#creazione oggetto risto1
risto1=Ristoranti("Trattoria da gino", "Sushi")

#menù opzioni
def opzioni():
    print("""\n1. Descrivi il ristorante
2. Visualizza stato apertura
3. Apri ristorante
4. Chiudi ristorante
5. Aggiungi piatto al menu
6. Togli piatto dal menu
7. Visualizza menù
0. Esci dal programma
""")

print("\n\n")
while True:
    opzioni()       #visualizzazione menù
    try:
        scelta=input("Inserisci la scelta: ")
    except :
        print("Errore")
        break
    if scelta=="1":                 #Descrivi il ristorante    
        risto1.descrivi_ristorante()
    elif scelta=="2":   #Visualizza stato apertura
        print("Il ristorante è: ", end="")
        risto1.stato_apertura()
    elif scelta=="3":   #Apri ristorante
        risto1.apri_ristorante()
        print("Il ristorante ora è: ", end="")
        risto1.stato_apertura()
    elif scelta=="4":   #Chiudi ristorante
        risto1.chiudi_ristorante()
        print("Il ristorante ora è: ", end="")
        risto1.stato_apertura()
    elif scelta=="5":       #Aggiungi piatto al menu
        try:
            piatto=input("Inserisci il nuovo piatto: ")
        except:
            print("Errore")
        try:
            costo=int(input("Inserisci il nuovo costo: "))
        except:
            print("Errore")
        risto1.aggiungi_al_menu(piatto, costo)
    elif scelta=="6":   #Togli piatto dal menu
        try:
            piatto=input("Inserisci il piatto da eliminare: ")
        except:
            print("Errore")
        risto1.togli_dal_menu(piatto)
    elif scelta=="7":   #Visualizza menù
        risto1.stampa_menu()
    elif scelta=="0":       #Esci dal programma
        exit()
    else:
        print("errore di scelta")

print("Chiusura programma. Arrivederci")
