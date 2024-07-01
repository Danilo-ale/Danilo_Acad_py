"""Create un gestionale per la vostra squadra di calcio, 
siete gli allenatori quindi potete aggiungere massimo 
25 calciatori:
- 3 portieri;
- 8 difensori;
- 8 centrocampisti;
- 6 attaccanti;
per ogni calciatore nome e ruolo.
Nel menù potete aggiungerli, eliminarli o visualizzarli, 
tutto verrà salvato in un database .txt

giocatori = tommaso,difensore\nantonio,attaccante\ndaniele,centrocampista\nalessio,portiere"
"""

n_giocatori = {"1":3, 
               "2":8, 
               "3":8, 
               "4":6}

conv_ruoli = { "1":"portiere",
              "2":"difensore",
              "3": "centrocampista",
              "4":"attaccante"}

def conta_ruolo(matrice, ruolo):
    numero = 0
    for element in matrice:
        if element[1] == ruolo:
            numero +=1
    return numero


def verifica_db():
    try:
        leggi_db()
    except:
        scrivi_db("", "w")


def leggi_db():
    with open("squadra.csv","r") as file:
        contenuto = file.read()
    return contenuto

def scrivi_db(dato, modo):
    with open("squadra.csv",modo) as file:
        file.write(dato)

def conv_matrice(dato):
    righe = dato.split("\n")
    if len(righe) <1:
        print("db vuoto!")
    elif len(righe) >1:
        righe_ok = []
        for riga in righe:
            righe_ok.append(riga.split(","))
    else:
        righe_ok = righe.split(",")
    return righe_ok

def conv_salvataggio(dato):
    if len(dato) >1:
        lista = []
        for riga in dato:
            lista.append(",".join(riga))
        stringa = "\n".join(lista)
    else:
        stringa = ",".join(dato)
    
    return stringa

def menu():
    print("Scivi 1 per aggiungere un giocatore\n2 per eliminare un giocatore\n3 per visualizzare i giocatori\n4 per uscire: ")

def inserisci_giocatore():
    contenuto = leggi_db()
    squadra_matri = conv_matrice(contenuto)
    if len(squadra_matri)> 24:
        print("Hai raggiunto il numero massimo di calciatori!")
    else:
        ruolo_ins = input("Inserisci 1 per portiere\n2 per difensore\n3 per centrocampista\n4 per attaccante: ")
        if ruolo_ins in n_giocatori:
            numero_massimo = n_giocatori[ruolo_ins]
            n_pres = conta_ruolo(squadra_matri, conv_ruoli[ruolo_ins])
            if n_pres >= numero_massimo:
                print("hai raggiunto il limite di calciatori per questo ruolo!")
            else:
                nome = input("Inserisci nome calciatore: ")
                squadra_matri.append([nome,conv_ruoli[ruolo_ins]])
                squadra_matri_str = conv_salvataggio(squadra_matri)
                scrivi_db(squadra_matri_str, "w")
                print("Giocatore inserito!")




        else:
            print("Ruolo non valido!")
    
def visualizza(matrice):
    for element in matrice:
        print(f"Nome: {element[0]}, Ruolo: {element[1]}")


def elimina_giocatore():
    contenuto = leggi_db()
    squadra_matri = conv_matrice(contenuto)
    nome = input("Inserisci nome calciatore: ")
    ruolo_ins = input("Inserisci 1 per portiere\n2 per difensore\n3 per centrocampista\n4 per attaccante: ")
    trovato = False
    for riga in squadra_matri:
        if riga[0] == nome and riga[1]== conv_ruoli[ruolo_ins]:
            squadra_matri.remove(riga)
            trovato = True
            squadra_matri_str = conv_salvataggio(squadra_matri)
            scrivi_db(squadra_matri_str, "w")
            print("Giocatore Eliminaro!")
    if not trovato:
        print("Giocatore non trovato!")


