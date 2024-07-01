"""
Banca con file .csv

"""



def datidb():                        

    with open("3 settimana\\credenziali2.txt", "r") as file:
       contenuto=file.read()
    print(contenuto)
    righe=contenuto.split("\n")
    dizionario={}
    for riga in righe:
        riga=riga.split(",")
        print(riga)
        nome,cognome,conto=riga[1],riga[2],riga[3]
        diz={'nome':nome, "cognome":cognome,"conto":int(conto)}
        dizionario[riga[0]]=diz
    print(dizionario)
    return dizionario

def menu():
    print("1. Preleva")
    print("2. Versamento")
    print("3. Visualizza conto")
    print("4. Esci")

def versamento(codice):
    vers=input("inserisci somma da versare: ")
    db[codice]["conto"]+=int(vers)
    print(db)
    aggiorna_file(db)

def aggiorna_file(db):
    lista=""
    space=","
    chiavi=list(db.keys())
    print("Ultima chiave: ",chiavi[-1])
    for codice in chiavi:
        if codice !=chiavi[-1]:
            lista+=str(codice)+space+str(db[codice]["nome"])+space+str(db[codice]["cognome"])+space+str(db[codice]["conto"])+"\n"
        else:
            lista+=str(codice)+space+str(db[codice]["nome"])+space+str(db[codice]["cognome"])+space+str(db[codice]["conto"])
    print(lista)
    with open("3 settimana\\credenziali2.txt", "w") as file:
        file.write(lista)

while True:
    db=datidb()
    print(list(db.keys()))
    cod_cliente=input("Inserisci codice cliente: ")
    if cod_cliente in db.keys():
        menu()
        scelta=input("Inserisci scelta: ")
        if scelta=="2":
            versamento(cod_cliente)
    scelta=input("Continuare? ").lower()
    if scelta!="si":
        break

