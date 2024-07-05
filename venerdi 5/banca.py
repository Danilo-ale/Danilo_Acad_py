"""Create un gestionale bancario basato sulla programmazione a oggetti, 
la prima parte dell'esercizio riguarda solamente aggiunta e 
eliminazione cliente con il suo conto bancario e modifica cliente"""

class Cliente:
    def __init__ (self, nome, età,carta_credito,cvc,saldo=0):

        self.__nome=nome
        self.__età=età
        self.__carta_credito=carta_credito
        self.__cvc=cvc
        self.__saldo=float(saldo)

    def get_nome(self): 
        return self.__nome
    
    def get_cvc(self):
        return self.__cvc

    def get_saldo(self):
        return self.__saldo

    def deposito(self, importo):
        importo=float(importo)
        self.__saldo+=importo
        print(f"Deposito di {importo} euro effettuato.")
    
    def set_nome(self, nome):
        self.__nome = nome

    def preleva(self, importo):
        importo=float(importo)
        if importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelievo di {importo} euro effettuato.")
        else:
            print(f"Saldo insufficiente per effettuare il prelievo. Saldo corrente: {self.get_saldo()}")

    def paga(self, importo):
        importo=float(importo)
        if importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Pagamento di {importo} euro effettuato.")
        else:
            print(f"Saldo insufficiente per effettuare il pagamento. Saldo corrente: {self.get_saldo()}")

class GestoreBanca(Cliente):
    def __init__(self):
        self.__clienti = []
    
    def aggiungi_cliente(self, nome, eta, carta_credito, cvc, saldo=0):
        trovato = False
        for cliente in self.__clienti:
            if cvc == cliente.get_cvc():
                trovato=True
        if trovato == False:
            nuovo_cliente=Cliente(nome,eta,carta_credito,cvc,saldo)
            self.__clienti.append(nuovo_cliente)
            print("Cliente aggiunto con successo.")

        else:
            print("Codice CVC già presente. ")
    
    def pagamento(self,nome,cvc,importo):
        trovato = False
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                cliente.paga(importo)               
                trovato=True
        if trovato == False:
            print("Cliente non trovato")

    def prelievo(self,nome,cvc,importo):
        trovato = False
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                cliente.preleva(importo)               
                trovato=True
        if trovato == False:
            print("Cliente non trovato")
    

    def deposito(self,nome,cvc,importo):
        trovato = False
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                cliente.deposito(importo)               
                trovato=True
        if trovato == False:
            print("Cliente non trovato")

    def rimuovi_cliente(self, nome, cvc):
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                self.__clienti.remove(cliente)
                print("Cliente rimosso.")
            else:
                print("Cliente non registrato")
    
    def modifica_nome(self,nome,cvc,nuovo_nome):
        trovato = False
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                cliente.set_nome(nuovo_nome)                
                trovato=True
        if trovato == True:
            print("Hai modificato il nome")
        else:
            print("Utente non trovato")
    
    def lista_clienti(self):
        for cliente in self.__clienti:
            print(f"Lista clienti: {cliente.get_nome()}. Saldo: {cliente.get_saldo()}")
        

def menu():
    print("""\n1. Apri conto
2. Chiudi conto
3. Modifica cliente
4. Lista clienti
5. Pagamento
6. Deposito
7. Prelievo          
0. Esci
""")
    

banca=GestoreBanca()
banca.aggiungi_cliente("Pino",45, "1234", "123", 1000)

while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        while True:
            nome=input("Inserisci il nome del nuovo cliente: ")
            if nome.isalpha():
                break
            else:
                print("Inserisci solo lettere: ")
        while True:
            try:
                eta=int(input("Inserisci l'età del cliente: "))
                break
            except:
                print("ERRORE")
        while True:
            try:
                carta_credito=int(input("Inserisci il numero della carta di credito: "))
                break
            except:
                print("ERRORE")
        while True:
            cvc=input("Inserisci il cvc della carta: ")
            if len(cvc)!=3:
                print("cvc non conforme: ")
            else:
                break
        banca.aggiungi_cliente(nome, eta,carta_credito,cvc)
    elif scelta=="2":       #RIMUOVI CLIENTE
        nome=input("Inserisci il nome del cliente: ")
        cvc=int(input("Inserisci il cvc della carta: "))
        banca.rimuovi_cliente(nome,cvc)
    elif scelta=="3":
        nome=input("Inserisci il vecchio nome del cliente: ")
        cvc=int(input("Inserisci il cvc della carta: "))
        nuovo_nome=input("Inserisci il nuovo nome del cliente: ")
        banca.modifica_nome(nome,cvc,nuovo_nome)
    elif scelta == "4":
        banca.lista_clienti()
    elif scelta=="5":
        nome=input("Inserisci il nome del cliente: ")
        cvc=int(input("Inserisci il cvc della carta: "))
        importo=input("Inserisci l'importo da pagare: ")
        banca.pagamento(nome,cvc,importo)
    elif scelta=="6":
        nome=input("Inserisci il nome del cliente: ")
        cvc=int(input("Inserisci il cvc della carta: "))
        importo=float(input("Inserisci l'importo da depositare: "))
        banca.deposito(nome,cvc,importo)
    elif scelta=="7":
        nome=input("Inserisci il nome del cliente: ")
        cvc=int(input("Inserisci il cvc della carta: "))
        importo=input("Inserisci l'importo da prelevare: ")
        banca.prelievo(nome,cvc,importo)
    elif scelta=="0":
        break