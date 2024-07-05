from random import randint 

class Pokemon:
    mosse=["Azione"]
    def __init__(self, nome):
        self.nome=nome

class Pokedeck:
    def __init__(self):
        self.lista_ogg=[]
        self.diz_cont={}
        self.diz_cont["Acqua"]=0
        self.diz_cont["Terra"]=0
        self.diz_cont["Elettro"]=0
        self.diz_cont["Fuoco"]=0

    def aggiungi_pok(self,pokem):
        trovato=False
        for pokemon in self.lista_ogg:
            if pokemon.get_nome()==pokem.get_nome():
                trovato=True
        if trovato==False:
            self.lista_ogg.append(pokem)
            self.diz_cont[pokem.get_tipo()]+=1




def menu():
    print("""1. Aggiungi pokemon al pokedeck
2. 
3.
4.
5.          
""")


p1=Pikachù("Gino")
p2=Pikachù("Nico")

pok1=Pokedeck()     #POKEDECK

def tipi_pok():
    print("1. Pikachu")
    print("2. Charmender")
    print("3. Squirtle")
    print("4. Bulbasaur")

while True:
    menu()
    scelta=input("Seleziona una scelta: ")
    if scelta=="1":     
        tipi_pok()
        scelta=input("Seleziona un tipo di pokemon: ")
        if scelta=="1":         #Pikachu
            nome=input("Inserisci il nome del pokemon: ")
            ogg_pik=Pikachù("NOME")        #creazione pikachu
            pok1.aggiungi_pok(ogg_pik)
        elif scelta=="2":       #Charmender
            pass        #creazione Charmender

        elif scelta=="3":       #Squirtle
            pass        #creazione Squirtle

        elif scelta=="4":       #Bulbasaur
            pass        #creazione Bulbasaur
        else:
            print("Scelta sbagliata.")

    elif scelta=="2":
        pass
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")