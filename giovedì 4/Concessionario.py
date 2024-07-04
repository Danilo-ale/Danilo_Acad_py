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
        return self.stato_richiesta     #equivale a "sì" o "no" per indicare se richiesto (true) o no (false). 

    
    def get_stato_vendita(self):
        return self.stato_vendita   ##equivale a "sì" o "no" per indicare se venduta (true) o no (false). 
    
    #metodo per riassunto caratteristiche auto
    def mostra(self):           #GLI IF TRASFORMANO TRUE O FALSE IN "Sì" O "NO"
        if self.get_richiesta()==True:
            self.stato_richiesta="Sì"
        else:
            self.stato_richiesta="No"
        if self.get_venduto()==True:
            self.stato_vendita="Sì"
        else:
            self.stato_vendita="No"
        return f"TIPO:{self.get_tipo()}--> {self.get_marca()} {self.get_modello()}. Anno {self.get_anno()}. Venduta? {self.get_stato_vendita()}. Richiesta? {self.get_stato_richiesta()}"

#CLASSE CONCESSIONARIO
class Concessionario(Auto):
    def __init__(self, nome):
        self.__nome=nome
        self.lista_ogg=[]
        self.auto_ric=[]        #LISTA AUTO RICHIESTE PER LA VENDITA
        self.quant_auto_ric=[]  #LISTA PARALLELA (PER MEMORIZZARE LE QUANTITA' DELLA RICHIESTA)

        self.auto_ric_nol=[]    #LISTA AUTO RICHIESTA PER IL NOLEGGIO
        self.quant_auto_ric_nol=[]  #LISTA PARALLELA (PER MEMORIZZARE LE QUANTITA' DELLA RICHIESTA)


    def aggiungi_veicolo(self, veicolo):        #AGGIUNGE VEICOLO
        self.lista_ogg.append(veicolo)
    
    #GETTER NOME CONCESSIONARIO
    def get_nome(self):
        return self.__nome
    
    def __str__(self) -> str:
        return f"Benvenuto al Concessionario di 🚗 {self.get_nome()} 🚗. Come posso aiutarti?"

    #VISUALIZZA LE AUTO RICHIESTE PER LA VENDITA
    def visualizza_auto_richieste(self):
        if len(self.auto_ric)>0:
            print("Auto richieste per vendita: ")
            for auto in self.auto_ric:
                print(f"--> {auto}. Richiesta: {self.quant_auto_ric[self.auto_ric.index(auto)]} volta/e")
        else:
            print("---Nessun auto richiesta per la vendita ⚠️ ---")
        
        #VISUALIZZA LE AUTO RICHIESTE PER IL NOLEGGIO
        if len(self.auto_ric_nol)>0:
            print("Auto richieste per noleggio: ")
            for auto in self.auto_ric_nol:
                print(f"-->{auto}. Richiesta {self.quant_auto_ric_nol[self.auto_ric_nol.index(auto)]} volta/e")
        else:
            print("---Nessun auto per noleggio richiesta ⚠️ ---")

    #AGGIUNGE LE AUTO CHE VENGONO RICHIESTE PER LA VENDITA NELL'APPOSITA LISTA
    def lista_auto_richieste_vendita(self, marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                stringa=marca+" "+modello
                if stringa not in self.auto_ric:
                    self.auto_ric.append(stringa)
                    self.quant_auto_ric.append(1)
                else:
                    self.quant_auto_ric[self.auto_ric.index(stringa)]+=1
                veicolo.set_richiesta()
                trovato=True
        if trovato:
            print("Veicolo per vendita richiesto ✅")
        else:
            print("Veicolo non trovato ❌")
        
    def lista_auto_richieste_noleggio(self, marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                stringa=marca+" "+modello
                if stringa not in self.auto_ric_nol:
                    self.auto_ric_nol.append(stringa)
                    self.quant_auto_ric_nol.append(1)
                else:
                    self.quant_auto_ric_nol[self.auto_ric.index(stringa)]+=1
                veicolo.set_richiesta()
                trovato=True
        if trovato:
            print("Veicolo per noleggio richiesto ✅")
        else:
            print("Veicolo non trovato ❌")

    def lista_veicoli(self):
        if len(self.lista_ogg)>0:
            for veicolo in self.lista_ogg:
                print(veicolo.mostra())
        else:
            print("Nessuno veicolo presente in concessionaria ⚠️")
    def rimuovi_veicoli(self, marca, modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                self.lista_ogg.remove(veicolo)
                trovato=True
        if trovato:
            print("Veicolo rimosso ✅")
        else:
            print("Veicolo non trovato ❌")
    
    def vendi_veicolo(self,marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello and veicolo.get_venduto()==False:
                veicolo.set_venduto()
                trovato=True
        if trovato:
            print("Veicolo venduto ✅")
        else:
            print("Veicolo non trovato o già venduto❌")

def menu_conc():
    print("""\n1. Visualizza veicoli concessionario
2. Aggiungi auto
3. Rimuovi veicolo
4. Vendi veicolo
5. Visualizza auto richieste
0. Esci
""")
conc1=Concessionario("AutoHero")
a1=Auto("audi", "a4", 2010, 5)
conc1.aggiungi_veicolo(a1)

def titolare():
    print("~~~SEZIONE PRIVATA~~~")
    print(conc1)
    while True:
        menu_conc()
        scelta=input("Inserisci un'opzione: ")
        if scelta=="1":
            conc1.lista_veicoli()
        elif scelta=="2":
            marca=input("Inserisci la marca del veicolo: ")
            modello=input("Inserisci il modello del veicolo: ")
            while True:
                try:
                    anno=int(input("Inserisci l'anno del veicolo: "))
                    break
                except ValueError as e:
                    print("Errore: ",e)
            while True:
                try:
                    n_porte=int(input("Inserisci il numero di porte del veicolo: "))
                    break
                except ValueError as e:
                    print("Errore ",e)
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
    print("""\n1. Visualizza veicoli concessionario
2. Richiedi vendita auto
3. Richiedi auto a noleggio
0. Esci 
""")

def cliente():
    print(conc1)
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
