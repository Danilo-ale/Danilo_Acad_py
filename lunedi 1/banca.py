"""
Banca con file .csv

"""



def verifica_utente(nome,cognome,password):                         #verifica credenziali
    ver=False
    with open("3 settimana\\credenziali.txt", "r") as file:
        contenuto=file.read()
    righe=contenuto.split("\n")
    for riga in righe:
        riga=riga.split(",")
        if password== riga[0] and nome ==riga[1] and cognome==riga[2]:
            ver= True
    return ver


#menu
def menu():
    print("1. Preleva")
    print("2. Versamento")
    print("3. Visualizza conto")
    print("4. Esci")

def preleva(nome,cognome,password):
    with open("3 settimana\\credenziali.txt", "r") as file:
        contenuto=file.read()
    righe=contenuto.split("\n")
    lista=""
    for riga in righe:
        riga=riga.split(",")
        if password== riga[0] and nome ==riga[1] and cognome==riga[2]:
            prelievo=input("inserisci somma da prelevare: ")
            prelievo=int(prelievo)
            if prelievo <=int(riga[3]):
                riga[3]=int(riga[3])
                riga[3]-=prelievo
                riga[3]=str(riga[3])
        riga=",".join(riga)
        lista=lista+riga+"\n"
    with open("3 settimana\\credenziali.txt", "w") as file:   #aggiornamento file
        file.write(lista)


def versamento(nome,cognome,password):
    with open("3 settimana\\credenziali.txt", "r") as file:         #versamento
        contenuto=file.read()
    righe=contenuto.split("\n")
    lista=""
    for riga in righe:
        riga=riga.split(",")
        if password== riga[0] and nome ==riga[1] and cognome==riga[2]:
            vers=int(input("Inserisci somma da versare: "))
            riga[3]=int(riga[3])+vers
            riga[3]=str(riga[3])
        riga=",".join(riga)    
        lista=lista+riga+"\n"
        with open("3 settimana\\credenziali.txt", "w") as file:   #aggiornamento file
            file.write(lista)  


def visualizza_conto(nome,cognome,password):
    with open("3 settimana\\credenziali.txt", "r") as file:         #versamento
        contenuto=file.read()
    righe=contenuto.split("\n")
    lista=""
    for riga in righe:
        riga=riga.split(",")
        if password== riga[0] and nome ==riga[1] and cognome==riga[2]:
           print(f"Nome cliente: {nome}, Cognome: {cognome}, Conto: {riga[3]}")

while True:
    nome=input("Inserisci nome: ")
    cognome=input("inserisci cognome: ")
    password=input("Inserisci password: ")
    ver=verifica_utente(nome,cognome,password)
    if ver==True:
        while True:
            menu()
            scelta=input("Inserisci una scelta: ")
            if scelta=="1":
                preleva(nome,cognome,password)
            elif scelta=="2":
                versamento(nome,cognome,password)
            elif scelta=="3":
                visualizza_conto(nome,cognome,password)
            elif scelta=="4":
                exit()
            else:
                print("Selezione sbagliata")
            scelta=input("Continuare con lo stesso cliente? ")
            if scelta.lower()!="si":
                break
    else:
        print("Cliente non presente")
    scelta=input("Continuare con il programma? ")
    if scelta.lower()!="si":
        break
        
    


#print(database)


#print(database)