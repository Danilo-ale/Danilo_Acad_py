#classe Partita IVA
class Partive_iva:
    nome=""
    cognome=""
    data_inizio=""
    
    def __init__(self, nome, data_inizio):       #costruttore oggetto
        self.nome=nome
        self.data_inizio=data_inizio
    def __str__(self):  
        return f"Nome titolare \"{self.nome}\", data inizio attività: {self.data_inizio}" 


#classe cliente
class Clienti:

    def __init__(self, nome, cognome):
        self.nome=nome
        self.cognome=cognome
    
    def ordina(self):
        piatto=input("Inserisci piatto da ordinare: ")

        self.ordine=Ordini(self.nome, self.cognome, piatto)
    def __str__(self):
        return f"Nome cliente \"{self.nome}\", cognome: \"{self.cognome}\""
    
    def ordini_cliente(self):
        print(self.ordine.getOrdini())

        
class Ordini:           #CLASSE ORDINI, CONTIENE LISTA DEGLI ORDINI
    ordini=[]
    def __init__(self, nome_cliente, cogn_cliente, piatto):
        self.nome=nome_cliente
        self.cognome=cogn_cliente
        Ordini.ordini.append(piatto)
    
    def getOrdini(self):
        return Ordini.ordini
    

#classe ristoranti
class Ristoranti:           
    nome=""
    tipo_cucina=""
    def __init__(self, nome,tipo_cucina):       #costruttore
        self.menu={}
        self.nome=nome
        self.tipo_cucina=tipo_cucina
        self.aperto=False
        """try:        #try except per inserimento nome titolare
            nome_titotare=input("Inserisci il nome del titolare: ")
        except:
            print("Errore nell'inserimento del nome titolare.")
        while True:         #ripete il ciclo fino a quando l'utente inserisce il formato di data corretto 
            try:
                anno,mese,giorno=input("Inserisci data nel formato AAAA-MM-GG: ").split("-")
                break
            except:
                print("Formato errato.")"""
        data="2023"+"-"+"08"+"-"+"09"       #concatenamento formato data [TEMPORANEO]
        nome_titolare="gino"
        self.p_iva=Partive_iva(nome_titolare,data)      #costruzione nuovo oggetto Partita IVA
    def descrivi_ristorante(self):  #funzione descrivi
        print(f"Benvenuto al ristorante \"{self.nome}\". Il suo tipo di cucina è \"{self.tipo_cucina}\" \nDettagli ristorante: {self.p_iva.__str__()}")

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
            self.menu[piatto]=costo     #inserimento del nuovo piatto e costo nel dizionario
        else:
            print("Piatto già presente!")       #se è già presente, visualizza un messaggio di avviso, 
            #ma chiede se si vuole scambiare il prezzo nel menu con quello inserito
            scelta=input(f"Vuoi forse modificare il prezzo del piatto \"{piatto}\" da {self.menu[piatto]} in {costo}? ").lower()
            if scelta=="si":
                self.menu[piatto]=costo     #se risponde sì, si modifica il costo del piatto
                print("Prezzo modificato!")
            else:
                print("Uscita dall'opzione")    #altrimenti si esce senza fare alcuna modifica
    def togli_dal_menu(self,piatto):        #funzione elimina piatto dal menù
        if piatto in self.menu.keys():      #verifica che non sia già presente nel menu
            del self.menu[piatto]       #rimozione piatto dal dizionario
            print("Piatto eliminato!")
        else:
            print("Piatto non presente")

    def stampa_menu(self):
        if len(self.menu)>0:        #verifica che ci sia effettivamente almeno un piatto nel dizionario
            print("\nPiatti presenti:")
            for piatto in self.menu.keys():
                print(f"{piatto}, costo: {self.menu[piatto]}")  #visualizzazione nome e costo di ciascun piatto 
        else:
            print("Menù vuoto!")
    def getPartitaIva(self):
        return self.p_iva.__str__()
            
#creazione oggetto risto1
risto1=Ristoranti("Trattoria da gino", "Sushi")     #dopo questa istruzione viene richiesta la

#print(risto1.p_iva)

#menù opzioni
def opzioni():
    print("""\n1. Descrivi il ristorante
2. Visualizza stato apertura
3. Apri ristorante
4. Chiudi ristorante
5. Aggiungi piatto al menu
6. Togli piatto dal menu
7. Visualizza menù
8. Visualizza dettagli Partita IVA
0. Esci dal programma
""")
    
def opz_cliente():
    print("""\n1. Descrivi il ristorante
2. Visualizza menù
3. Ordina piatto
4. Visualizza lista ordini
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
    elif scelta=="8":
        print(risto1.getPartitaIva())
    elif scelta=="0":       #Esci dal programma
        break
    else:
        print("errore di scelta")

print("Chiusura programma gestionale. Apertura programma cliente:")

print("Creazione cliente: ")
nome=input("Inserisci nome cliente: ")
cognome=input("Inserisci cognome del cliente: ")

cliente1=Clienti(nome,cognome)
while True:
    opz_cliente()
    scelta=input("Inserisci scelta: ").lower()
    if scelta=="1":
        risto1.descrivi_ristorante()
    elif scelta=="2":       #visualizza menu
        risto1.stampa_menu()
    elif scelta=="3":
        cliente1.ordina()
    elif scelta=="4":
        cliente1.ordini_cliente()
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")

print("CHIUSURA PROGRAMMA")