import random as r          #import libreria per choice

#CREAZIONE SUPERCLASSE
class MembroSquadra:
    def __init__(self, nome, età):
        self.nome=nome
        self.età=età
    

    def descrivi(self):
        return f"Membro squadra: {self.nome}, età: {self.età}"
    
#CREAZIONE CLASSE FIGLIO
class Giocatore(MembroSquadra):
    def __init__(self, nome, età, ruolo, numero_maglia):
        super().__init__(nome, età)     #richiamo super costruttore
        self.ruolo=ruolo    #aggiunta attributi specifici del figlio
        self.numero_maglia=numero_maglia
        self.gioca_partita=False
    
    def gioca_partita(self):        #attributo diventa true
        self.partita_giocata=True
    
    def descrivi(self):     #descrizione giocatore, con override
        self.descrizione=MembroSquadra.descrivi(self) +", ruolo:"+self.ruolo
        return self.descrizione

#CREAZIONE CLASSE FIGLIO  
class Allenatore(MembroSquadra):
    def __init__(self, nome, età, anni_exp):
        super().__init__(nome, età)     #richiamo super costruttore
        self.anni_exp=anni_exp      #aggiunta attributi specifici del figlio
    
    def dirige_allenamento(self):        #metodo per indicare che ha svolto l'allenamento
        print("Allenamento svolto")


#CREAZIONE CLASSE FIGLIO
class Assistente(MembroSquadra):
    def __init__(self, nome, età, specializzazione):
        super().__init__(nome, età)                 #richiamo super costruttore
        self.specializzazione=specializzazione      #aggiunta attributi specifici del figlio
        self.operazioni=[]      #lista operazioni che può effettuare vuota
    
    def supporta_Team(self):        
        if len(self.operazioni)>0:      #se la lista contiene qualcosa, sceglie un'operazione random
            return f"L'assistente {self.nome} ha supportato il team con un/una {r.choice(self.operazioni)}"
        else:
            return f"L'assistente {self.nome} non ha effettuato nessun operazione, grande incapace"
        
    def Aggiugni_operazione(self, operazione):      #permette di aggiungere le operazioni che l'assistente può effettuare
        self.operazioni.append(operazione)

#creazione oggetti
ms1=MembroSquadra("gino",20)
g1=Giocatore("DiLivio", 20, "Centravanti di sfondamento","20")
a1=Allenatore("Acciughina Allegri", 70, 30)
as1=Assistente("Pino il postino", 20, "polpette al sugo")

#alla prima chiamata non restituisce nessuna operazione. perché il suo attributo lista è vuoto
print(as1.supporta_Team())
#aggiunta operazioni all'assistente
as1.Aggiugni_operazione("Lasagna")
as1.Aggiugni_operazione("Massaggiatore")
#richiamata alla funzione di prima, ora stampa una delle due operazioni aggiunte
print(as1.supporta_Team())

#richiamo funzione allenamento
a1.dirige_allenamento()
print(g1.descrivi())