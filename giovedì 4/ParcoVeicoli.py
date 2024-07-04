class Veicolo:
    #COSTRUTTORE CLASSE PADRE
    def __init__(self, marca, modello, anno):
        self.__marca=marca
        self.__modello=modello
        self.__anno=anno
        self.__accensione=False
    
    #METODO PER CAMBIARE VALORE ALLA VARIABILE
    def __accendi(self):
        self.__accensione=True
    #METODO PER ACCENDERE
    def acceso(self):
        self.__accendi()
        print("Veicolo Acceso")
    
    def __spegni(self):
        self.__accensione=False
    #GETTER 
    def get_modello(self):  # Metodo getter pubblico
        return self.__modello

    def get_marca(self):
        return self.__marca 
    
    def modifica_marca(self,marca):
        self.__marca=marca
    
    def get_anno(self):
        return self.__anno

#CLASSE FIGLIO AUTO 
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte=numero_porte
    #METOOD PER SUONARE IL CLACSON
    def suona_clacson(self):
        print("BEEEEEP")
    #GETTER E SETTER
    def get_tipo(self):
        return "Auto"
    
    def __set_marca(self,marca):
        self.__marca=marca
    
    def mod_marca(self,marca):
        self.modifica_marca(marca)
    #metodo per riassunto caratteristiche auto
    def mostra(self):
        return f"TIPO:{self.get_tipo()}--> {self.get_marca()} {self.get_modello()}. Anno {self.get_anno()}"
    
    

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacità_carico):
        super().__init__(marca, modello, anno)
        self.__capacità_carico=capacità_carico
        self.carico=False

    def get_tipo(self):
        return "Furgone"

    def mod_marca(self,marca):
        self.modifica_marca(marca)

    def mostra(self):
        return f"TIPO:{self.get_tipo()}--> {self.get_marca()} {self.get_modello()}."

    def carica(self):
        if self.carico==False:
            print("Il furgone si sta caricando")
            self.carico=True
        else:
            print("Furgone già carico")

    def scarica(self):
        if self.carico==True:
            print("Il furgone si sta scaricando")
            self.carico=False
        else:
            print("Furgone già scarico")
    

class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.__tipo=tipo.lower()
    
    def get_tipo(self):
        return "Motocicletta"
    
    def mod_marca(self,marca):
        self.modifica_marca(marca)

    def esegui_wheelie(self):
        if self.__tipo=="sportivo":
            print("La moto sta eseguendo uno wheelie")
        else:
            print("La moto non può eseguire dei wheelie")
    def mostra(self):
        return f"TIPO:{self.get_tipo()}--> {self.get_marca()} {self.get_modello()}"


class GestoreParcoVeicoli(Auto, Motocicletta, Furgone):
    def __init__(self, nome):
        self.__nome=nome
        self.__parco_veicoli={}
        self.__parco_veicoli["Auto"]=0
        self.__parco_veicoli["Furgone"]=0
        self.__parco_veicoli["Motocicletta"]=0

        self.lista_ogg=[]

    def aggiungi_veicolo(self, veicolo):
        self.lista_ogg.append(veicolo)
        self.__parco_veicoli[veicolo.get_tipo()]+=1
    
    def lista_veicoli(self):
        for veicolo in self.lista_ogg:
            print(veicolo.mostra())
    
    def accendi_veicolo(self,marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:
            
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                veicolo.acceso()
                trovato=True
        if trovato==False:
            print("Veicolo non presente")
    
    def clacson_veicolo(self,marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:
            
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello and veicolo.get_tipo()=="Auto":
                veicolo.suona_clacson()
                trovato=True
        if trovato==False:
            print("Auto non presente")

    def lista_diz(self):
        for tipo in self.__parco_veicoli.keys():
            print(f"Tipo: {tipo}. Numero veicoli: {self.__parco_veicoli[tipo]}")

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

    def cambia_marca(self,marca,modello,nuova_marca):
        trovato=False
        for veicolo in self.lista_ogg:          
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                veicolo.mod_marca(nuova_marca)
                trovato=True
        if trovato:
            print("Veicolo modificato")
        else:
            print("Veicolo non trovato")
    def impenna(self,marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:
            
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello and veicolo.get_tipo()=="Motocicletta":
                veicolo.esegui_wheelie()
                trovato=True
        if trovato==False:
            print("Moto non presente")

    def carica_furgone(self,marca,modello):
        trovato=False
        for veicolo in self.lista_ogg:     
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello and veicolo.get_tipo()=="Furgone":
                veicolo.carica()
                trovato=True
        if trovato==False:
            print("Furgone non presente")
        
    
g1=GestoreParcoVeicoli("Carburatori & co.")
a1=Auto("Toyota","Prius",2020, 10)

g1.aggiungi_veicolo(a1)
f1=Furgone("Ford","Furgonone",2020, 100)
g1.aggiungi_veicolo(f1)
m1=Motocicletta("yamaha", "9GT", 2007, "sportivo")
g1.aggiungi_veicolo(m1)
g1.lista_veicoli()

g1.lista_veicoli()

def menu():
    print("""1. Aggiungi veicolo
2. Rimuovi veicolo
3. Visualizza lista veicoli dettagliata
4. Visualizza lista veicoli generica
5. Accendi veicolo
6. Suona clacson
7. Cambia marca di un veicolo
8. Esegui wheelie con una moto
9. Carica il furgone
0. Esci dal programma
""")
    

while True:
    menu()
    scelta=input("Inserisci un'opzione: ")
    if scelta=="1":
        marca=input("Inserisci la marca del veicolo da inserire: ")
        modello=input("Inserisci il modello del veicolo da inserire: ")
        anno=int(input("Inserisci l'anno del veicolo da inserire: "))
        tipo=input("Inserisci il tipo del veicolo: ")
        if tipo=="auto":
            n_porte=int(input("Inserisci il numero di portiere: "))
            ogg=Auto(marca,modello,anno,n_porte)
            g1.aggiungi_veicolo(ogg)
        elif tipo=="furgone":
            cap_carico=int(input("Inserisci la capacità di carico del furgone: "))
            ogg=Furgone(marca,modello,anno,cap_carico)
            g1.accendi_veicolo(ogg)
        elif tipo=="motocicletta":
            tipologia=input("Inserisci la tipologia della moto: ")
            ogg=Motocicletta(marca,modello,anno,tipologia)
            g1.accendi_veicolo(ogg)
    elif scelta=="2":
        m_rim=input("Inserisci marca del veicolo da rimuovere: ")
        mod_rim=input("Inserisci il modello del veicolo da rimuovere: ")
        g1.rimuovi_veicoli(m_rim,mod_rim)
    elif scelta=="3":
        g1.lista_veicoli()
    elif scelta=="4":
        g1.lista_diz()
    elif scelta=="5":
        m_acc=input("Inserisci marca del veicolo da accendere: ")
        mod_acc=input("Inserisci il modello del veicolo da accendere: ")
        g1.accendi_veicolo(m_acc, mod_acc)
    elif scelta=="6":
        m_acc=input("Inserisci marca dell'auto: ")
        mod_acc=input("Inserisci il modello dell'auto: ")
        g1.clacson_veicolo(m_acc, mod_acc)
    elif scelta=="7":
        m_mod=input("Inserisci marca del veicolo da modificare: ")
        mod_mod=input("Inserisci il modello del veicolo da modificare: ")
        nuova_marca=input(f"Inserisci la nuova marca del veicolo {mod_mod}: ")
        g1.cambia_marca(m_mod, mod_mod, nuova_marca)
    elif scelta=="8":
        m_acc=input("Inserisci marca della moto da impennare: ")
        mod_acc=input("Inserisci il modello della moto da impennare: ")      
        g1.impenna(m_acc,mod_acc)
    elif scelta=="9":
        m_acc=input("Inserisci la marca del furgone da caricare: ")
        mod_acc=input("Inserisci il modello del furgone da caricare: ")     
        g1.carica_furgone(m_acc,mod_accul)       
    elif scelta=="0":
        break
    else:
        print("scelta sbagliata")