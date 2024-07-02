class Fabbriche:
    def __init__(self, nome):           #COSTRUTTORE FABBRICA
        self.lista=[]
        self.lista_prod=[]
        self.invent={}
        self.nome=nome
        self.guadagno=0
    
    def aggiungi_prodotto(self):     #AGGIUNGI PRODOTTO
        nome_prod=input("Inserisci il nome del prodotto: ")
        if nome_prod not in self.invent.keys():     #VERIFICA CHE IL NOME DEL PRODOTTO NON SIA NEL DIZIONARIO
            self.invent[nome_prod]=1        #AGGIUNGE IL PRODOTTO AL DIZIONARIO 

            prod=Prodotti(nome_prod)        #CREA IL NUOVO OGGETTO PRODOTTI
            self.lista.append(prod)         #memorizza nella lista gli oggetti
            self.lista_prod.append(nome_prod)   #memorizza nella lista parallela i nomi degli oggetti
            print("PRODOTTO AGGIUNTO!\n")
            #print(self.lista)

        else:
            self.invent[nome_prod]+=1       #se è già presente nel dizionario, aggiunge una quantità
    
    def vendi_prodotto(self, nome_prod):        #VENDITA PRODOTTO
        if nome_prod not in self.invent.keys():     #se non c'è nel dizionario, stampa messaggio di errore
            print("Prodotto non presente nell'inventario!")
        elif self.invent[nome_prod]==0:     #se la quantità del prodotto ==0, visualizza messaggio di errore di vendita
            print("Quantità prodotto insufficiente")
        else:
            self.invent[nome_prod]-=1       #altrimenti scala una quantità dal prodotto
            print("PRODOTTO VENDUTO! Profitto: ", end="")
            if prod in self.lista_prod:
                print(self.lista[self.lista_prod.index(prod)].calcola_profitto())
                self.guadagno+=self.lista[self.lista_prod.index(prod)].calcola_profitto()



    def resi_prodotto(self, nome_prod):     #RESI DEL PRODOTTO
        if nome_prod not in self.invent.keys():     #se il prodotto non è nel dizionario, lo crea
            self.invent[nome_prod]=1
            print("PRODOTTO AGGIUNTO!\n")
        else:
            self.invent[nome_prod]+=1       #altrimenti aggiunge una quantità alla chiave già esistente
            print("QUANTITA' PRODOTTO AGGIORNATA!\n")

    
    #STAMPA L'INVENTARIO
    def vis_inventario(self):
        if len(self.invent)>0:
            for prod in self.invent.keys():
                print(f"Nome prodotto {prod}, quantità: {self.invent[prod]}")
        else:
            print("INVENTARIO VUOTO \n")
    
    def getGuadagno(self):
        return self.guadagno

#CLASSE ELETTRONICA
class Elettronica:
    def __init__(self, nome):       
        self.nome=nome
        self.garanzia=input("Inserisci la garanzia del prodotto: ")       #INSERIMENTO GARANZIA

class Abbigliamento:
    def __init__(self, nome):
        self.nome=nome
        self.materiale=input("Inserisci il materiale del prodotto: ")   #INSERIMENTO MATERIALE DEL PRODOTTO


class Prodotti:
    def __init__(self, nome):
        self.nome=nome
        #self.costo_prod=costo_prod
        #self.prezzo_vend=prezzo_vend
        self.costo_prod=input("Inserisci il costo di produzione: ")   #chiede il costo di prod  
        self.prezzo_vend=input("Inserisci il prezzo di vendita: ")  #chiede il costo di vendita
        scelta=input("Scegli tipologia prodotto:\n1. Abbigliamento   2. Elettronica: ")   #scelta per creare un oggetot elettronica o abbigliamento
        if scelta=="1":
            self.tipologia=Abbigliamento(self.nome)
        elif scelta=="2":
            self.tipologia=Elettronica(self.nome)
    
    #METODO CALCOLO DEL PROFITTO
    def calcola_profitto(self):
        return int(self.prezzo_vend)-int(self.costo_prod)


fb1=Fabbriche("Il paradiso della brugola")

def menu():
    print("""
1. Aggiungi prodotto
2. Vendi prodotto
3. Resi prodotto
4. Visualizza inventario
0. Esci
""")
    
while True:
    menu()
    scelta=input("Seleziona un'opzione: ")
    if scelta=="1":
        fb1.aggiungi_prodotto()
    elif scelta=="2":
        prod=input("Inserisci il prodotto da vendere: ")
        fb1.vendi_prodotto(prod)
    elif scelta=="3":
        prod=input("Inserisci il prodotto da rendere: ")
        fb1.resi_prodotto(prod)
    elif scelta=="4":
        fb1.vis_inventario()
    elif scelta=="0":
        break
    else:
        print("scelta sbagliata")


print(f"Il guadagno della giornata è: {fb1.getGuadagno()}")
print("CHIUSURA PROGRAMMA")