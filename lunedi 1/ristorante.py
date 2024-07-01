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
        self.menu[piatto]=costo
    def togli_dal_menu(self,piatto):
        if piatto in self.menu.keys():
            del self.menu[piatto]
        else:
            print("Piatto non presente")

    def stampa_menu(self):
        print("\nPiatti presenti:")
        for piatto in self.menu.keys():
            print(f"{piatto}, costo: {self.menu[piatto]}")

risto1=Ristoranti("Trattoria da gino", "Sushi")
#risto1.stampa_menu()

def opzioni():
    print("""1. Descrivi il ristorante
2. Visualizza stato apertura
3. Apri ristorante
4. Chiudi ristorante
5. Aggiungi piatto al menu
6. Togli piatto dal menu
7. Visualizza menù
""")


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
risto1.stampa_menu()
