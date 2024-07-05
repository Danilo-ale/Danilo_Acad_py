"""
Create un gestionale bancario basato sulla programmazione a oggetti, 
la prima parte dell'esercizio riguarda solamente aggiunta e eliminazione cliente con il suo conto bancario
e modifica cliente
"""
class Cliente:

    def __init__(self, nome, età,carta_credito,cvc):

        self.__nome=nome
        self.__età=età
        self.__carta_credito=carta_credito
        self.__cvc=cvc



def menu():
    print("""\n1. Apri conto
2. Chiudi conto
3. Modifica cliente
0. Esci
""")
    

banca=GestioneBanca()

while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        while True:
            nome=input("Inserisci il nome del nuovo cliente: ")
            if nome.isalpha():
                break
            else:
                print("Inserisci solo lettere")
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
                print("cvc non conforme")
            else:
                break
        nuovo_cliente=Cliente(nome, eta,carta_credito,cvc)
        banca=aggiungi_cliente(nuovo_cliente)
    elif scelta=="2":
        pass
    elif scelta=="3":
        pass
    elif scelta=="0":
        break