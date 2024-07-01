class Ristoranti:
    nome=""
    tipo_cucina=""
    def __init__(self, nome,tipo_cucina):
        self.menu={}
        self.nome=nome
        self.tipo_cucina=tipo_cucina
        self.aperto=False
    def descrivi_ristorante(self):
        print(f"Benvenuto al ristorante \"{self.nome}\". Il suo tipo di cucina è \"{self.tipo_cucina}\"")

    def stato_apertura(self):
        if self.aperto==False:
            print("chiuso")
        else:
            print("aperto")
            
    def apri_ristorante(self):
        self.aperto=True
    def chiudi_ristorante(self):
        self.aperto=False
    
    def aggiungi_al_menu(self,piatto,costo):
        if piatto not in self.menu.keys():
            self.menu[piatto]=costo
        else:
            print("Piatto già presente!")
    def togli_dal_menu(self,piatto):
        if piatto in self.menu.keys():
            del self.menu[piatto]
        else:
            print("Piatto non presente")

    def stampa_menu(self):
        if len(self.menu)>0:
            print("\nPiatti presenti:")
            for piatto in self.menu.keys():
                print(f"{piatto}, costo: {self.menu[piatto]}")
        else:
            print("Menù vuoto!")

risto1=Ristoranti("Trattoria da gino", "Sushi")
#risto1.stampa_menu()

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

"""
    risto1.descrivi_ristorante()
    print("Il ristorante è: ", end="")
    risto1.stato_apertura()
    risto1.apri_ristorante()
    print("Il ristorante ora è: ", end="")
    risto1.stato_apertura()
    risto1.chiudi_ristorante()
    print("Il ristorante ora è: ", end="")
    risto1.stato_apertura()
    risto1.aggiungi_al_menu("trofie al pesto", 50)
    risto1.aggiungi_al_menu("Pasta", 80)
    risto1.stampa_menu()
    risto1.togli_dal_menu("Pasta")
    risto1.stampa_menu()"""
print("\n\n")
while True:
    opzioni()
    try:
        scelta=input("Inserisci la scelta: ")
    except :
        print("Errore")
        break
    if scelta=="1":
        risto1.descrivi_ristorante()
    elif scelta=="2":
        print("Il ristorante è: ", end="")
        risto1.stato_apertura()
    elif scelta=="3":
        risto1.apri_ristorante()
        print("Il ristorante ora è: ", end="")
        risto1.stato_apertura()
    elif scelta=="4":
        risto1.chiudi_ristorante()
        print("Il ristorante ora è: ", end="")
        risto1.stato_apertura()
    elif scelta=="5":
        try:
            piatto=input("Inserisci il nuovo piatto: ")
        except:
            print("Errore")
        try:
            costo=int(input("Inserisci il nuovo piatto: "))
        except:
            print("Errore")
        risto1.aggiungi_al_menu(piatto, costo)
    elif scelta=="6":
        try:
            piatto=input("Inserisci il piatto da eliminare: ")
        except:
            print("Errore")
        risto1.togli_dal_menu("Pasta")
    elif scelta=="7":
        risto1.stampa_menu()
    elif scelta=="0":
        exit()
    else:
        print("errore di scelta")

