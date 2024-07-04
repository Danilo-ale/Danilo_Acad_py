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

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte=numero_porte
    
    def suona_clacson(self):
        print("BEEEEEP")
    
    def __get_tipo(self):
        return "Auto"

    def __get_marca(self):
        return self.__marca

    def __get_modello(self):
        return self.__modello
"""    
    def __str__(self) -> str:
        return f"Tipo veicolo: {self.get_tipo()}. {self.__marca} {self.__modello}. """

class Furgone(Veicolo):
    pass

class Motocicletta(Veicolo):
    pass

class GestoreParcoVeicoli(Auto):
    def __init__(self, nome):
        self.__nome=nome
        self.__parco_veicoli={}
        self.__parco_veicoli["Auto"]=0
        self.__parco_veicoli["Furgone"]=0
        self.__parco_veicoli["Motocicletta"]=0

        self.lista_ogg=[]

    def aggiungi_veicolo(self, veicolo):
        self.lista_ogg.append(veicolo)
        #self.__parco_veicoli[veicolo.__get_tipo()]+=1
    
    def lista_veicoli(self):
        for veicolo in self.lista_ogg:
            print( f"Tipo veicolo: {veicolo.__get_tipo()}. {veicolo.__get_tipo()} {veicolo.__get_modello()}. ")
        
    
g1=GestoreParcoVeicoli("Carburatori & co.")
a1=Auto("Toyota","Prius",2020, 10)
g1.aggiungi_veicolo(a1)

g1.lista_veicoli()