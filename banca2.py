"""
Banca con file .csv

"""



def datidb():                        
    #lettura dei dati dal file. Li prelievo e li inserisco in un dizionario
    with open("3 settimana\\lunedi 1\\credenziali2.txt", "r") as file:
       contenuto=file.read()
    print(contenuto)
    righe=contenuto.split("\n")
    dizionario={}
    for riga in righe:
        riga=riga.split(",")
        print(riga)
        nome,cognome,conto=riga[1],riga[2],riga[3]
        diz={'nome':nome, "cognome":cognome,"conto":int(conto)}
        dizionario[riga[0]]=diz        #riga[0] contiene il codice del cliente, che è univoco. A questa chiave associo il dizionario relativo
    #print(dizionario)
    return dizionario

def menu():
    print("1. Preleva")
    print("2. Versamento")
    print("3. Visualizza conto")
    print("4. Esci")
    

#versamento 
def versamento(codice):
    vers=input("inserisci somma da versare: ")
    db[codice]["conto"]+=int(vers)
    print(db)
    aggiorna_file(db)

#aggiorno il file da riscrivere sul file di testo
def aggiorna_file(db):
    lista=""
    virg=","
    chiavi=list(db.keys())
    print("Ultima chiave: ",chiavi[-1])
    for codice in chiavi:
        if codice !=chiavi[-1]:     #se il codice_cliente equivale all'ultimo, non mette \n. Altrimenti la ri-lettura del file genera un errore di index
            lista+=str(codice)+virg+str(db[codice]["nome"])+virg+str(db[codice]["cognome"])+virg+str(db[codice]["conto"])+"\n"
        else:
            lista+=str(codice)+virg+str(db[codice]["nome"])+virg+str(db[codice]["cognome"])+virg+str(db[codice]["conto"])
    #print(lista)
    with open("3 settimana\\credenziali2.txt", "w") as file:
        file.write(lista)

while True:
    db=datidb()    #db conterrà il dizionario ritornato dalla funzione
    
    cod_cliente=input("Inserisci codice cliente: ")    #login molto veloce (per debug). chiede solo il codice cliente
    if cod_cliente in db.keys():
        menu()
        scelta=input("Inserisci scelta: ")
        if scelta=="1":
            pass
        elif scelta=="2":        #per il momento solo la scelta del versamento è disponibile
            versamento(cod_cliente)
        elif scelta=="3":
            pass
        elif scelta=="4":
            exit()
        else:
            print("Selezione sbagliata.")
    scelta=input("Continuare? ").lower()
    if scelta!="si":
        break

