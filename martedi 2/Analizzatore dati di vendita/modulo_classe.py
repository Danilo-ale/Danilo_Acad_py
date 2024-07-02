"""
I dati di vendita sono rappresentati come una lista di numeri,
 dove ciascun numero rappresenta l'importo totale delle vendite in un giorno specifico. 
 Il tuo programma dovrebbe fare quanto segue:
Requisiti:

-Inserimento dei Dati: Chiedi all'utente di inserire una serie di importi di vendita, separati da spazi. 
    Converti questi importi in una lista di numeri interi.
-Gestione delle Eccezioni: Durante la conversione degli importi in numeri interi, 
    gestisci qualsiasi ValueError che possa sorgere a causa di un inserimento errato 
    (ad esempio, l'utente inserisce una lettera invece di un numero), informando l'utente dell'errore e chiedendogli di reinserire i dati.
-Calcolo del Totale e della Media: Calcola il totale e la media delle vendite. 
    Stampa entrambi i valori con un messaggio appropriato. Se la lista è vuota (ad esempio, se l'utente non inserisce alcun dato),
      stampa un messaggio che indica che non sono presenti dati di vendita.
-Vendite Sopra la Media: Trova e stampa una lista di tutti i giorni in cui le vendite hanno superato 
    la media delle vendite di tutto il periodo. Assicurati di gestire correttamente 
        il caso in cui non ci siano vendite sopra la media.
-Visualizzazione dei Risultati: Per ogni punto sopra, stampa 
    i risultati in modo chiaro e leggibile, con messaggi appropriati 
        che spiegano cosa sta mostrando il programma.

"""
#CLASSE VENDITA
class Vendite:
    def __init__(self, stringa):    #COSTRUTTORE
        self.lista=[]
        self.lista=self.conversione(stringa)    #LA LISTA RICHIAMA IL METODO CONVERSIONE, CHE RITORNA UNA LISTA SE SONO TUTTI NUMERI, altrimenti ERROR
    
    def conversione(self, stringa): #METODO CONVERSIONE
        self.conv=[]
        self.conv=stringa.split(" ")    #SPLIT DELLA STRINGA IN INPUT
        self.lista2=[]
        for num in self.conv:   
            try:                #VERIFICA CHE SIANO EFFETTIVAMENTE NUMERI 
                num=int(num)
                self.lista2.append(num)
            except ValueError as e:
                print("Errore", e)  #ALTRIMENTI RITORNA ERROR
                return "ERROR"
        return self.lista2

    def calcolo_totale(self):       #calcolo del totale
        if len(self.lista)>0:           #se la lunghezza della lista >1, ritorna il totale
            self.totale=sum(self.lista)
            return f"Il totale delle vendite è: {self.totale}"
 
        else:       #altrimenti ritorna un messaggio di errore
            return "Lista vuota. Nessun totale."
    
    def calcolo_media(self):        #CALCOLO MEDIA
        if len(self.lista)>0:
            self.media= self.totale/len(self.lista)     #CALCOLO MEDIA
            return f"La media delle vendite è: {self.media}"    #RETURN del valore della media
        else:
            return "Lista vuota. Nessuna media."
    
    def vend_sopra_media(self):
        self.vend_media=[]      #lista giorni vendite sopra la media
        for numero in self.lista:       #per ogni numero della lista
            if numero>self.media:       #verifica che sia > di self.media
                self.vend_media.append(self.lista.index(numero)+1)      #se sì, aggiunge alla lista il giorno della vendita superiore della media
        if len(self.vend_media)>0:      #se la lista è riempita, la stampa
            return f"I giorni sopra la media sono: {self.vend_media}"
        else:       #altrimenti stampa un messaggio di avviso
            return f"Nessun numero sopra la media"