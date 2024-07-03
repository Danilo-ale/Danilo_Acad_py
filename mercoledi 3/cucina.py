from random import sample
#CLASSE PADRE
class PersonaleCucina:
    def __init__(self,nome,età):
        self.nome=nome
        self.età=età
    

    def lavora(self):
        return f"{self.nome} sta svolgendo un lavoro non specificato"
    
class Chef(PersonaleCucina):
    def __init__(self, nome, età, specialità,ingredienti):
        super().__init__(nome, età)
        self.specialità=specialità

        self.ingredienti=ingredienti.split(",")
    
    def __str__(self) -> str:
        return f"Benvenuto nel ristorante di {self.nome}. La sua specialità è {self.specialità}"
        

    def prepara_menu(self):
        if len(self.ingredienti)>1:
            nuovo_piatto=sample(self.ingredienti,2)
            return f"Lo chef {self.nome} ha preparato {nuovo_piatto[0]} e {nuovo_piatto[1]}"
        else:
            return f"Lo chef {self.nome} ha preparato {self.ingredienti}"
    
class SousChef(PersonaleCucina):
    def __init__(self, nome, età, specializzazione):
        super().__init__(nome, età)
        self.specializzazione=specializzazione
        self.dispensa=[]
        self.disp_quantità=[]

    def aggiungi_in_dispensa(self,elemento, quantità):
        self.dispensa.append(elemento)
        self.disp_quantità.append(quantità)
    
    def gestisci_dispensa(self):
        if len(self.dispensa)==0:
            print("Dispensa vuota 😓")
        elif len(self.dispensa)==1:
            print("La dispensa ha solo un elemento 😅", end="")
            print(f"--> Unico elemento: {self.dispensa[0]}")
        else:
            print("Elementi ordinati: ",sorted(self.dispensa))
        
    def assisti_chef(self):
        self.spesa={}
        for elemento in self.disp_quantità:
            if elemento < 5:
                self.spesa[self.dispensa[self.disp_quantità.index(elemento)]]=elemento
        
        if len(self.spesa)>0:
            for ingrediente in self.spesa.keys():
                print(f"-->Ingrediente carente: {ingrediente}. Quantità rimasta: {self.spesa[ingrediente]}")

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, età):
        super().__init__(nome, età)    
        self.preparazione={}

    def cucina_piatto(self, piatto):
        if piatto in self.preparazione.keys():
            print(f"La preparazione di {piatto} è {self.preparazione[piatto]}")   
        else:
            print(f"Piatto non presente nella memoria di {self.nome}")

    def aggiungi_preparazione(self, piatto, prep):
        if piatto in self.preparazione.keys():
            print(f"Il piatto è gia presente nel dizionario.")
            scelta=input(f"Vuoi cambiare la preparazione di \"{piatto}\" in \"{prep}\"?")
            if scelta.lower()=="si":
                self.preparazione[piatto]=prep
        else:
            self.preparazione[piatto]=prep
            print("\n\nPiatto aggiunto nella lista!")

pc1=PersonaleCucina("Pino",99)
ch1=Chef("Gino lo scugnizzo", 20, "Cucina thailandese", "polpette,pasta,pane e panelle,panino con la milza,arrosticini")
print(ch1)

print(ch1.prepara_menu())

sc1=SousChef("Manny", 30, "Tutto fare")
#PRINTA DISPENSA VUOTA
sc1.gestisci_dispensa()

elemento=input("Aggiungi un ingrediente in dispensa: ").lower()
while True:
    try:
        quantità=int(input("Aggiungi la quantità dell'ingrediente: "))
        break
    except:
        print("Errore nell'inserimento, reinserisci")

sc1.aggiungi_in_dispensa(elemento,quantità)
sc1.gestisci_dispensa()


sc1.aggiungi_in_dispensa("pasta",4)
sc1.gestisci_dispensa()

sc1.assisti_chef()
cl1=CuocoLinea("Pino",11)

piatto=input("\n\nInserisci il piatto di cui vuoi sapere la preparazione: ").lower()
cl1.cucina_piatto(piatto)

piatto=input("\n\nInserisci il piatto da inserire in memoria: ").lower()
prep=input(f"Inserisci la preparazione di {piatto}: ")
cl1.aggiungi_preparazione(piatto,prep)
cl1.aggiungi_preparazione(piatto,"cucinalo benissimo")


cl1.cucina_piatto(piatto)