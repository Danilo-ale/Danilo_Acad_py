"""Esercizio 1 (Facile): Scrivi una funzione chiamata area_triangolo
 che prenda in input la base e l'altezza di un triangolo e
   restituisca la sua area. fare la stessa cosa con quadrato e 
   rettagolo e rendere ripetibile salvando in una lista tutti i 
   risultati

"""
def area_triangolo():                   #FUNZIONE TRIANGOLO
    while True: 
        base=input("Inserisci la base: ")           # inserimento dati
        altezza=input("Inserisci l'altezza: ")
        if (base.isnumeric() and altezza.isnumeric()):  #controllo correttezza dati
            break
        else:
            print("Inserisci dei numeri.")

    return (int(base)*int(altezza))/2      #return area

def area_quadrato():
    while True:
        lato=input("Inserisci il lato: ")   # inserimento dati
        if (lato.isnumeric()):      #controllo correttezza dati
            break
        else:
            print("Inserisci un numero.")
    lato=int(lato)          #casting del dato (era stringa prima)
    return lato*lato

def area_rettangolo():
    while True:
        base=input("Inserisci la base: ")       # inserimento dati
        altezza=input("Inserisci l'altezza: ")
        if (base.isnumeric() and altezza.isnumeric()):  #controllo correttezza dati
            break
        else:
            print("Inserisci dei numeri.")
    base=int(base)      #casting del dato (era stringa prima)
    altezza=int(altezza)    #casting del dato (era stringa prima)
    return base*altezza         #return area

risultati=[]
while True:
    print("menù")       #menù
    print("1. Area triangolo")   
    print("2. Area quadrato")
    print("3. Area rettangolo")
    print("4. Visualizza storico risultati")
    scelta=input("Scegli una delle opzioni: ")
    if scelta=="1":
        area=area_triangolo()   #calcolo area triangolo
        print("Area del triangolo è:",area)
        risultati.append(area)  #aggiunta nella lista
    elif scelta=="2":
        area=area_quadrato()        #calcolo area quadrato
        print("Area del quadrato è:",area)
        risultati.append(area)  #aggiunta nella lista
    elif scelta=="3":
        area=area_rettangolo()      ##calcolo area rettangolo
        print("Area del rettangolo è:",area)
        risultati.append(area)      #aggiunta nella lista
    elif scelta=="4":
        print("Visualizzazione storico: ")
        for i in risultati:
            print(i)            #visualizza dati in lista
    else:
        print("Scelta sbagliata.")
    scelta=input("Continuare? ").lower()
    if scelta!="si":
        break
print("chiusura")