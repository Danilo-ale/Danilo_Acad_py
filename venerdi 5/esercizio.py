from random import randint, choice
class Pokemon:
    def __init__(self):
        self.__nome=""

    def stampa_nome(self):
        print(f"Il nome di questo pokemon è {self.__nome}")

    def set_nome(self):
        self.__nome = input("Indicare il nome del Pokemon: ")

    def get_nome(self):
        return self.__nome

class Pikachù(Pokemon):
    razza = "Pikachù"
    tipo = "Elettro"
    hp = 50

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Fulmine":25}

    def attacca_casuale(self):      #attacca casuale pokemon selvatico
        lista_attacchi=list(self.mosse.keys())
        mossa=choice(lista_attacchi)
        print(f"Il pokemon selvatico ha eseguito: \"{mossa}\"")
        return self.mosse[mossa]     

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Fulmine\n")
            if a == "1":
                attacco = self.mosse["Azione"]
                print("Azione")
                return attacco
            elif a == "2":
                attacco = 15
                print("Attacco rapido")
                return attacco
            elif a == "3":
                attacco = 25
                print("Fulmine")
                return attacco
            else:
                print("Errore")
    
    def info(self):
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Squirtle(Pokemon):
    razza = "Squirtle"
    tipo = "Acqua"
    hp = 60

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Pistol acqua":25}

    def attacca_casuale(self):      #attacca casuale pokemon selvatico
        lista_attacchi=list(self.mosse.keys())
        mossa=choice(lista_attacchi)
        print(f"Il pokemon selvatico ha eseguito: \"{mossa}\"")
        return self.mosse[mossa]       

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Pistol acqua\n")
            if a == "1":
                attacco = 20
                print("Azione")
                return attacco
            elif a == "2":
                attacco = 15
                print("Attacco rapido")
                return attacco
            elif a == "3":
                attacco = 25
                print("Pistol acqua")
                return attacco
            else:
                print("Errore")
    
    def info(self):
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Bulbasaur(Pokemon):
    razza = "Bulbasaur"
    tipo = "Erba"
    hp = 55

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Fendi foglia":25}

    def attacca_casuale(self):      #attacca casuale pokemon selvatico
        lista_attacchi=list(self.mosse.keys())
        mossa=choice(lista_attacchi)
        print(f"Il pokemon selvatico ha eseguito: \"{mossa}\"")
        return self.mosse[mossa]     
            
    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Fendi foglia\n")
            if a == "1":
                attacco = 20
                print("Azione")
                return attacco
            elif a == "2":
                attacco = 15
                print("Attacco rapido")
                return attacco
            elif a == "3":
                attacco = 25
                print("Fendi foglia")
                return attacco
            else:
                print("Errore")
    
    def info(self):
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Charmander(Pokemon):
    razza = "Charmander"
    tipo = "Fuoco"
    hp = 45

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Lancia fiamme":25}

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Lancia fiamme\n")
            if a == "1":
                attacco = 20
                print("Azione")
                return attacco
            elif a == "2":
                attacco = 15
                print("Attacco rapido")
                return attacco
            elif a == "3":
                attacco = 25
                print("Lancia fiamme")
                return attacco
            else:
                print("Errore")

    def attacca_casuale(self):      #attacca casuale pokemon selvatico
        lista_attacchi=list(self.mosse.keys())
        mossa=choice(lista_attacchi)
        print(f"Il pokemon selvatico ha eseguito: \"{mossa}\"")
        return self.mosse[mossa]   

    
    def info(self):
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Pokedex:
    def __init__(self):
        self.lista_ogg=[]
        self.diz_cont={}
        self.diz_cont["Acqua"]=0
        self.diz_cont["Erba"]=0
        self.diz_cont["Elettro"]=0
        self.diz_cont["Fuoco"]=0

    def aggiungi_pok(self,pokem):
        trovato=False
        for pokemon in self.lista_ogg:
            if pokemon.get_nome()==pokem.get_nome():
                trovato=True
        if trovato==False:
            self.lista_ogg.append(pokem)
            self.diz_cont[pokem.tipo]+=1
            print("E' stato aggiunto con successo!")
        else:
            print("Il pokemon con questo nome è già presente nel pokedex")
        
    def ritorna_pok(self):
        pass


def menu():
    print("1. Ricerca e cattura Pokemon\n2.Visualizza Pokedex\n")

pok1=Pokedex()     #POKEDECK

def tipi_pok():
    print("1. Pikachu")
    print("2. Charmender")
    print("3. Squirtle")
    print("4. Bulbasaur")

while True:
    tipi_pok()
    print("Scegli il tuo Pokemon iniziale: ")
    scelta=input("Seleziona una scelta: ")
    if scelta=="1":     
        if scelta=="1":         #Pikachu
            ogg_pik=Pikachù()
            ogg_pik.set_nome()
            pok1.aggiungi_pok(ogg_pik)
            break
        elif scelta=="2":       #Charmender
            ogg_pik=Charmander()
            ogg_pik.set_nome()
            pok1.aggiungi_pok(ogg_pik)        #creazione Charmender
            break
        elif scelta=="3":       #Squirtle
            ogg_pik=Squirtle()
            ogg_pik.set_nome()
            pok1.aggiungi_pok(ogg_pik)        #creazione Squirtle
            break
        elif scelta=="4":       #Bulbasaur
            ogg_pik=Bulbasaur()
            ogg_pik.set_nome()
            pok1.aggiungi_pok(ogg_pik)        #creazione Bulbasaur
        else:
            print("Scelta sbagliata.")

print(pok1.lista_ogg)
print(pok1.diz_cont)

print("IL GIOCO CONTINUA")



def ricerca_cattura():
    print("E' stato avvistato un Pokemon:")
    scelta=randint(1,4)
    if scelta==1:     #genera Pikachu
        pokemon=Pikachù()
    elif scelta==2:      #genera Charmander
        pokemon=Charmander()
    elif scelta==3:       #genera squirtle
        pokemon=Squirtle()
    elif scelta==4:       #genera Bulbasaur
        pokemon=Bulbasaur()
    
    pokemon.info()

    scelta=input("Vuoi attaccarlo? ").lower()
    if scelta=="si":        #DEVE SCEGLIERE IL POKEMON
        hp_mio_pok=ogg_pik.hp
        hp_nemico=pokemon.hp
        while hp_mio_pok>0 and hp_nemico>0:
            ns_att=ogg_pik.attacca()
            hp_nemico-=ns_att
            nem_att=pokemon.attacca_casuale()
            hp_mio_pok-=nem_att
        if hp_nemico <=0:
            scelta=input("HAI VINTO! Vuoi aggiungere il pokemon nel pokedex? ").lower()
            if scelta=="si":
                pokemon.set_nome()
                pok1.aggiungi_pok(pokemon)
            else:
                print("Va bene")
        else:
            print("Hai perso.")

                
    

while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        ricerca_cattura()
    elif scelta=="2":
        pass
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")