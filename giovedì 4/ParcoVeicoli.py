class Veicolo:
    def __init__(self, marca, modello, anno):
        self.__marca=marca
        self.__modello=modello
        self.__anno=anno
        self.__accensione=False
    
    def __accendi(self):
        self.__accensione=True
    
    def __spegni(self):
        self.__accensione=False
    
    def get_modello(self):  # Metodo getter pubblico
        return self.__modello

    def get_marca(self):
        return self.__marca 

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte=numero_porte
    
    def suona_clacson(self):
        print("BEEEEEP")
    
    def get_tipo(self):
        return "Auto"

    """
    def __get_modello(self):
        return self.get_modello"""

    def mostra(self):
        return f"TIPO:{self.get_tipo()}--> {self.get_marca()} {self.get_modello()}"
    
    

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacità_carico):
        super().__init__(marca, modello, anno)
        self.__capacità_carico=capacità_carico
        self.carico=False

    def get_tipo(self):
        return "Furgone"

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

    def esegui_wheelie(self):
        if self.__tipo=="sportivo":
            print("La moto sta eseguendo wheelie")
        else:
            print("La moto non può eseguire wheelie")
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

    def rimuovi_veicoli(self, marca, modello):
        for veicolo in self.lista_ogg:
            trovato=False
            if veicolo.get_marca()==marca and veicolo.get_modello()==modello:
                self.lista_ogg.remove(veicolo)
                trovato=True
        if trovato:
            print("Veicolo rimosso")
        else:
            print("Veicolo non trovato")
            

        
    
g1=GestoreParcoVeicoli("Carburatori & co.")
a1=Auto("Toyota","Prius",2020, 10)
g1.aggiungi_veicolo(a1)
f1=Furgone("Ford","Furgonone",2020, 100)
g1.aggiungi_veicolo(f1)
m1=Motocicletta("yamaha", "9GT", 2007, "sportivo")
g1.aggiungi_veicolo(m1)
g1.lista_veicoli()
m_rim=input("Inserisci marca del veicolo da rimuovere: ")
mod_rim=input("Inserisci il modello del veicolo da rimuovere: ")
g1.rimuovi_veicoli(m_rim,mod_rim)
g1.lista_veicoli()