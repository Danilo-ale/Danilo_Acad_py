class Teatro:
    #costruttore teatro
    def __init__(self, nome):
        self.__nome=nome
        self.__lista_posti=[]


    def prenota_posto(self):        #PRENOTA POSTO
        if len(self.__lista_posti)>0:       #CONTROLLA SE CI SONO POSTI CREATI
            prenotato=False
            numero=int(input("Inserisci il numero del posto che vuoi prenotare:  "))        #INPUT
            fila=input("Inserisci la fila del posto che vuoi prenotare: ")
            for posto in self.__lista_posti:
                if posto.get__numero()==numero and posto.get__fila()==fila and posto.get__stato()==False:       #CONTROLLA CHE IL POSTO ESISTA E SIA LIBERO
                    posto.prenota()
                    prenotato=True
            if prenotato:
                print("Posto prenotato")            #OUTPUT
            else:
                print("Posto non prenotato. Numero, o fila sbagliati. O posto già occupato")
        else:
            print("Nessun posto registrato")        
        
    
    def stampa_posti_occupati(self):        #STAMPA I POSTI OCCUPATI
        self.__posti_occupati=[]
        for posto in self.__lista_posti:    
            if posto.get__stato()==True:
                self.__posti_occupati.append(posto)     #VERIFICA QUALE POSTO E' OCCUPATO E LO METTE NELLA LISTA
        
        if len(self.__posti_occupati)>0:        #SE NELLA LISTA POSTI_OCCUPATI C'E' QUALCOSA, LO STAMPA     
            print("Posti occupati:")
            for posto in self.__posti_occupati:
                print(f"Posto: {posto.get__fila()}{posto.get__numero()}")
        else:
            print("Tutti i posti liberi")
    
    def creaPosto(self):        #CREA IL POSTO (PER IL MOMENTO NESSUN POSTO VIP CREABILE)
        numero=int(input("Inserisci il numero del posto che vuoi creare:  "))
        fila=input("Inserisci la fila del posto che vuoi creare: ")
        posto=Posto(numero,fila)
        self.__lista_posti.append(posto)
    
    def stampa_posti(self):     #STAMPA TUTTI I POSTI 
        print("Posti nel teatro")
        if len(self.__lista_posti)>0:
            for posto in self.__lista_posti:
                print(f"{posto.get__numero()}{posto.get__fila()} | Stato: {posto.get__stato()}")
        else:
            print("Nessun posto creato in teatro")


class Posto:    #CLASSE POSTO
    #COSTRUTTORE
    def __init__(self, __numero, __fila):
        self.__numero=__numero
        self.__fila=__fila
        self.__occupato=False
    #METODI GETTER
    def get__stato(self):
        return self.__occupato
    
    def get__numero(self):
        return self.__numero
    
    def get__fila(self):
        return self.__fila
    #cambia lo stato del posto che viene prenotato
    def prenota(self):
        self.__occupato=True

class PostoVIP(Posto): #work in progress
    #costruttore
    def __init__(self, __numero, __fila, extra):
        super().__init__(__numero, __fila)
        self.__extra=extra      #extra disponibile per posti vip
    
    def prenota(self):
        self.__occupato=True
        print(f"Servizio extra rilasciato per questo posto: {self.__extra}")


t1=Teatro("Gianni")
t1.prenota_posto()
t1.creaPosto()
t1.creaPosto()
t1.stampa_posti()
t1.stampa_posti_occupati()
t1.prenota_posto()
t1.stampa_posti()
t1.stampa_posti_occupati()
