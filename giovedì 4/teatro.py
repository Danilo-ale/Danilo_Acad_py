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

    def libera_posto(self, __numero,__fila):
        if len(self.__lista_posti)>0:
            trovato=False
            for posto in self.__lista_posti:
                if posto.get__numero()==__numero and posto.get__fila()==__fila:
                    posto.libera()
                    trovato=True
            if trovato:
                print(f"Posto {__numero}{__fila} liberato.")
            else:
                print("Posto non presente in teatro")
        else:
            print("Nessun posto nel teatro")
    
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
        scelta=input("Che tipo di posto è? 1.Normale\n2.VIP\n3.Standard\nScelta: ")
        if scelta=="1":
            posto=Posto(numero,fila)
            self.__lista_posti.append(posto)
        elif scelta=="2":
            extra=input("Inserisci l'extra per questo posto VIP: ").lower()
            posto=PostoVIP(numero,fila,extra)
            self.__lista_posti.append(posto)
        elif scelta=="3":
            costo_extra=input("Inserisci il costo extra per questo posto: ") 
            posto=PostoStandard(numero,fila, costo_extra)
            self.__lista_posti.append(posto)

    def stampa_posti(self):     #STAMPA TUTTI I POSTI 
        
        if len(self.__lista_posti)>0:
            print("Posti nel teatro")
            for posto in self.__lista_posti:
                if posto.get__stato()==False:
                    print(f"{posto.get__numero()}{posto.get__fila()} | Stato: Libero. Tipologia Posto: {posto.get__tipo()}")
                else:
                    print(f"{posto.get__numero()}{posto.get__fila()} | Stato: Occupato. Tipologia Posto: {posto.get__tipo()}")
        else:
            print("Nessun posto creato in teatro")


class Posto:    #CLASSE POSTO
    #COSTRUTTORE
    def __init__(self, __numero, __fila):
        self.__numero=__numero
        self.__fila=__fila
        self.__occupato=False
        self.__tipo="Normale"
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
    
    def libera(self):
        self.__occupato=False

    def get__tipo(self):
        return self.__tipo

class PostoVIP(Posto): #work in progress
    #costruttore
    def __init__(self, __numero, __fila, extra):
        super().__init__(__numero, __fila)
        self.__extra=extra      #extra disponibile per posti vip
        self.__tipo="VIP"

    def get__stato(self):
        return super().get__stato()

    def libera(self):
        return super().libera()
    
    def get__numero(self):
        return super().get__numero()
    
    def get__fila(self):
        return super().get__fila()
    
    def get__tipo(self):
         return self.__tipo
    
    def prenota(self):
        super().prenota()
        print(f"posto vip prenotato---L'extra è: {self.__extra}")




class PostoStandard(Posto):
    def __init__(self, __numero, __fila, costo_extra):
        super().__init__(__numero, __fila)
        self.costo_extra=costo_extra        #COSTO EXTRA
        self.__tipo="Standard"

    def prenota(self):
        super().prenota()
        print(f"Posto {self.get__numero()}{self.get__fila()} \"Standard\" prenotato \n ")
    

    def get__stato(self):
        return super().get__stato()
    
    def get__numero(self):
        return super().get__numero()
    
    def get__fila(self):
        return super().get__fila()
    
    def get__tipo(self):
         return self.__tipo 
    
    def libera(self):
        return super().libera()



t1=Teatro("Gianni")
"""t1.prenota_posto()
#t1.creaPosto()
#t1.creaPosto()
t1.creaPosto()
t1.stampa_posti()
t1.stampa_posti_occupati()
t1.prenota_posto()
t1.stampa_posti()
t1.stampa_posti_occupati()
print("Ora libero il posto")
t1.libera_posto(10,"q")
t1.stampa_posti_occupati()"""

def menu():
    print("""1. Crea posto
2. Prenota Posto
3. Visualizza elenco di tutti i posti
4. Visualizza elenco posti occupati
5. Libera un posto
0. Esci dal programma
""")


#MENU INTERAZIONE UTENTE
while True:
    menu()
    scelta=input("Scegli un'opzione: ")
    if scelta=="1":
        t1.creaPosto()
    elif scelta=="2":
        t1.prenota_posto()
    elif scelta=="3":
        t1.stampa_posti()
    elif scelta=="4":
        t1.stampa_posti_occupati()
    elif scelta=="5":
        numero=input("Inserisci il numero del posto da liberare: ")
        fila=input("Inserisci la fila del posto da liberare: ")
        t1.libera_posto(numero,fila)
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")