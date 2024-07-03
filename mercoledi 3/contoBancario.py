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
cb1.visualizza_saldo()
cb1.set__titolare("Pino")
cb1.visualizza_saldo()

lista_conti=[]
lista_conti.append(cb1)
def menu():
    print("""1. Crea il tuo nuovo conto bancario
2. Entra nel tuo conto bancario
0. Per uscire
""")


while True:
    menu()
    scelta=input("Inserisci un'opzione: ")
    if scelta=="1":
        while True:
            titolare=input("Inserisci il nome del nuovo titolare: ").strip()
            if titolare!="":
                conto=int(input("Inserisci il saldo del tuo conto: "))
                c_ogg=ContoBancario(titolare, conto)
                lista_conti.append(c_ogg)
                break
            else:
                print("Nome non valido")

    elif scelta=="2":
        pass
    elif scelta=="0":
        break
    else:
        print("scelta sbagliata")

for conto in lista_conti:
    print(conto.get__titolare())