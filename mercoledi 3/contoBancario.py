class ContoBancario:
    def __init__(self, titolare, saldo):
        self.__titolare=titolare
        self.__saldo=saldo
    def deposita(self,importo):
        if importo>0:
            self.__saldo+=importo
            print("Deposito effettuato")
        else:
            print("L'importo è negativo")
    
    def preleva(self,importo):
        if importo<=self.__saldo and importo>0:
            self.__saldo-=importo
            print("Prelievo effettuato")
        else:
            print("Prelievo non effettuato")
    
    def get__titolare(self):
        return self.__titolare
    
    def set__titolare(self,titolare):
        self.__titolare=titolare

    
    def visualizza_saldo(self):
        print(f"Il saldo di {self.__titolare} è: {self.__saldo}")

cb1=ContoBancario("Gianni",300)
"""cb1.visualizza_saldo()
cb1.set__titolare("Pino")
cb1.visualizza_saldo()"""

lista_conti=[]
lista_conti.append(cb1)

#MENU UTENTE NON LOGGATO
def menu():
    print("""1. Crea il tuo nuovo conto bancario
2. Entra nel tuo conto bancario
0. Per uscire
""")

#funzione per login
def verifica_utente(nometit):
    ver=False
    for conto in lista_conti:
        if nometit==conto.get__titolare():      #CONFRONTA SE IL NOME E' PRESENTE NEI CONTI
            ver=True
    return ver,conto


#MENU UTENTE LOGGATO
def menu_utente():
    print("""1. Deposita nel conto
2. Preleva dal conto
3. Visualizza saldo
0. Esci""")


#FUNZIONE OPERAZIONI UTENTE
def operazioni_utente(conto):
    while True:
        menu_utente()
        scelta=input("Scegli un'opzione: ")
        if scelta=="1":     #DEPOSITO
            dep=int(input("Inserisci l'importo da depositare: "))
            conto.deposita(dep)
        elif scelta=="2":       #PRELIEVO
            prel=int(input("Inserisci l'importo da prelevare: "))
            conto.preleva(prel)
        elif scelta=="3":       #VISUALIZZA CONTO
            conto.visualizza_saldo()
        elif scelta=="0":
            break
        else:
            print("Scelta sbagliata")




while True:
    menu()          #MENU DI ACCESSO O REGISTRAZIONE
    scelta=input("Inserisci un'opzione: ")
    if scelta=="1":     #OPZIONE REGISTRATI
        while True:     #SI RIPETE FINCHE' SONO RISPETTATE LE CONDIZIONI (stringa!= "")
            titolare=input("Inserisci il nome del nuovo titolare: ").strip()
            if titolare!="":
                conto=int(input("Inserisci il saldo del tuo conto: "))
                c_ogg=ContoBancario(titolare, conto)
                lista_conti.append(c_ogg)
                break
            else:
                print("Nome non valido")

    elif scelta=="2":       #OPZIONE LOGIN
        nometit=input("Inserisci il nome del titolare: ")
        ver,conto=verifica_utente(nometit)    #VERIFICA UTENTE
        if ver:     #se ver è True, permette di effettuare operazioni sul conto
            operazioni_utente(conto)
        else:
            print("Login sbagliato")
    elif scelta=="0":
        break
    else:
        print("scelta sbagliata")
