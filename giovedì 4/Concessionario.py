class Veicolo:
    #COSTRUTTORE CLASSE PADRE
    def __init__(self, marca, modello, anno):
        self.__marca=marca
        self.__modello=modello
        self.__anno=anno
        self.__venduto=False
    
    #GETTER 
    def get_modello(self):  # Metodo getter pubblico
        return self.__modello

    def get_marca(self):
        return self.__marca 
    
    def get_anno(self):
        return self.__anno
    
    def set_venduto(self):
        self.__venduto=True
    
    def get_venduto(self):
        return self.__venduto

#CLASSE FIGLIO AUTO 
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte=numero_porte
        self.__richiesta=False  #se è stata richiesta da un cliente o no

    #GETTER E SETTER
    def get_tipo(self):
        return "Auto"

    def get_richiesta(self):
        return self.__richiesta
    
    def set_richiesta(self):
        self.__richiesta=True
    
    def get_stato_richiesta(self):
        return self.stato_richiesta

    
    def get_stato_vendita(self):
        return self.stato_vendita
    
    #metodo per riassunto caratteristiche auto
    def mostra(self):
        if self.get_richiesta()==True:
            self.stato_richiesta="si"
        else:
            self.stato_richiesta="no"
        if self.get_venduto()==True:
            self.stato_vendita="si"
        else:
            self.stato_vendita="no"
        return f"TIPO:{self.get_tipo()}--> {self.get_marca()} {self.get_modello()}. Anno {self.get_anno()}. Stato vendita: {self.get_stato_vendita()}. Stato Richiesta: {self.get_stato_richiesta()}"

class Concessionario(Auto):
    def __init__(self, nome):
        self.__nome=nome
        self.lista_ogg=[]
        self.auto_ric=[]
        self.auto_ric_nol=[]

    def aggiungi_veicolo(self, veicolo):
        self.lista_ogg.append(veicolo)

    def visualizza_auto_richieste(self):
        if len(self.auto_ric)>0:
            print("Auto richieste per vendita: ")
            for auto in self.auto_ric:
                print(auto)
        else:
            print("---Nessun auto richiesta per la vendita---")
        
        if len(self.auto_ric_nol)>0:
            print("Auto richieste per noleggio: ")
            for auto in self.auto_ric_nol:
                print(auto)
        else:
            print("---Nessun auto per noleggio richiesta---")

    def lista_auto_richieste_vendita(self, marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                stringa=marca+" "+modello
                self.auto_ric.append(stringa)
                veicolo.set_richiesta()
                trovato=True
        if trovato:
            print("Veicolo per vendita richiesto")
        else:
            print("Veicolo non trovato")
        
    def lista_auto_richieste_noleggio(self, marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                stringa=marca+" "+modello
                self.auto_ric_nol.append(stringa)
                veicolo.set_richiesta()
                trovato=True
        if trovato:
            print("Veicolo per noleggio richiesto")
        else:
            print("Veicolo non trovato")

    def lista_veicoli(self):
        if len(self.lista_ogg)>0:
            for veicolo in self.lista_ogg:
                print(veicolo.mostra())
        else:
            print("Nessuno veicolo presente in concessionaria")
    def rimuovi_veicoli(self, marca, modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                self.lista_ogg.remove(veicolo)
                trovato=True
        if trovato:
            print("Veicolo rimosso")
        else:
            print("Veicolo non trovato")
    
    def vendi_veicolo(self,marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                veicolo.set_venduto()
                trovato=True
        if trovato:
            print("Veicolo venduto")
        else:
            print("Veicolo non trovato")

def menu_conc():
    print("""\n1. Visualizza veicoli concessionario
2. Aggiungi auto
3. Rimuovi veicolo
4. Vendi veicolo
5. Visualizza auto richieste
0. Esco
""")
conc1=Concessionario("AutoHero")
a1=Auto("audi", "a4", 2010, 5)
conc1.aggiungi_veicolo(a1)

def titolare():
    while True:
        menu_conc()
        scelta=input("Inserisci un'opzione: ")
        if scelta=="1":
            conc1.lista_veicoli()
        elif scelta=="2":
            marca=input("Inserisci la marca del veicolo: ")
            modello=input("Inserisci il modello del veicolo: ")
            anno=input("Inserisci l'anno del veicolo: ")
            n_porte=input("Inserisci il numero di porte del veicolo: ")
            ogg=Auto(marca,modello,anno,n_porte)
            conc1.aggiungi_veicolo(ogg)
        elif scelta=="3":
            marca=input("Inserisci la marca del veicolo: ")
            modello=input("Inserisci il modello del veicolo: ")
            conc1.rimuovi_veicoli(marca,modello)
        elif scelta=="4":
            marca=input("Inserisci la marca del veicolo da vendere: ")
            modello=input("Inserisci il modello del veicolo da vendere: ")
            conc1.vendi_veicolo(marca,modello)
        elif scelta=="5":
            conc1.visualizza_auto_richieste()
        elif scelta=="0":
            break
        else:
            print("Scelta sbagliata.")



def menu_cliente():
    print("""1. Visualizza veicoli concessionario
2. Richiedi vendita auto
3. Richiedi auto a noleggio
0. Esci
""")

def cliente():
    print("Benvenuto nel concessionario")
    while True:       
        menu_cliente()
        scelta=input("Inserisci un'opzione: ")
        if scelta=="1":
            conc1.lista_veicoli()
        elif scelta=="2":
            marca=input("Inserisci la marca del veicolo da richiedere: ")
            modello=input("Inserisci il modello del veicolo da richiedere: ")
            conc1.lista_auto_richieste_vendita(marca,modello)
        elif scelta=="3":
            marca=input("Inserisci la marca del veicolo da richiedere: ")
            modello=input("Inserisci il modello del veicolo da richiedere: ")
            conc1.lista_auto_richieste_noleggio(marca,modello)
        elif scelta=="0":
            break
        else:
            print("Scelta sbagliata")

while True:
    utente=input("Sei 1.cliente o 2. titolare?\n0. per uscire\nScelta: ")
    if utente=="1":
        cliente()
    elif utente=="2":
        titolare()
    elif utente=="0":
        break
    else:
        print("Scelta sbagliata")
