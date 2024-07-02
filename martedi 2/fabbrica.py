class Fabbriche:
    def __init__(self, nome):           #COSTRUTTORE FABBRICA
        self.invent={}
        self.nome=nome
    
    def aggiungi_prodotto(self, nome_prod):     #AGGIUNGI PRODOTTO
        nome_prod=input("Inserisci il nome del prodotto: ")
        if nome_prod not in self.invent.keys():     #VERIFICA CHE IL NOME DEL PRODOTTO NON SIA NEL DIZIONARIO
            self.invent[nome_prod]=1        #AGGIUNGE IL PRODOTTO AL DIZIONARIO 
            self.prod=Prodotti(nome_prod)   #E CREA L'OGGETTO
        else:
            self.invent[nome_prod]+=1       #se è già presente nel dizionario, aggiunge una quantità
    
    def vendi_prodotto(self, nome_prod):        #VENDITA PRODOTTO
        if nome_prod not in self.invent.keys():     #se non c'è nel dizionario, stampa messaggio di errore
            print("Prodotto non presente nell'inventario!")
        elif self.invent[nome_prod]==0:     #se la quantità del prodotto ==0, visualizza messaggio di errore di vendita
            print("Quantità prodotto insufficiente")
        else:
            self.invent[nome_prod]-=1       #altrimenti scala una quantità dal prodotto
    
    def resi_prodotto(self, nome_prod):     #RESI DEL PRODOTTO
        if nome_prod not in self.invent.keys():     #se il prodotto non è nel dizionario, lo crea
            self.invent[nome_prod]=1
        else:
            self.invent[nome_prod]+=1       #altrimenti aggiunge una quantità alla chiave già esistente

#CLASSE ELETTRONICA
class Elettronica:
    def __init__(self, nome):       
        self.nome=nome
        self.garanzia=input("Inserisci la garanzia del prodotto")       #INSERIMENTO GARANZIA

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
        scelta=input("Scegli tipologia prodotto:\n1. Abbigliamento   2. Elettronica")   #scelta per creare un oggetot elettronica o abbigliamento
        if scelta=="1":
            self.tipologia=Elettronica(self.nome)
        elif scelta=="2":
            self.tipologia=Abbigliamento(self.nome)
    
    #METODO CALCOLO DEL PROFITTO
    def calcola_profitto(self):
        return self.prezzo_vend-self.costo_prod


fb1=Fabbriche("Il paradiso della brugola")

def menu():
    print("""
1. Aggiungi prodotto
2. Vendi prodotto
3. Resi_prodotto
0. Esci
""")
    
while True:
    menu()
    scelta=input("Seleziona un'opzione: ")
    if scelta=="1":
        pass
    elif scelta=="2":
        pass
    elif scelta=="3":
        pass
    elif scelta=="0":
        break
    else:
        print("scelta sbagliata")


print("CHIUSURA PROGRAMMA")
