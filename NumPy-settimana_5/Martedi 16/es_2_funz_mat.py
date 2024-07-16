"""Consegna:

1.Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2.Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
3.Somma i due array elemento per elemento per ottenere un nuovo array.
4.Calcola la somma totale degli elementi del nuovo array.
5.Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6.Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
"""
import numpy as np
#crea array della somma degli elementi dei due array
def crea_array_somma():
    somma_arr=np.zeros(50)      #creazioe array posto = 0 inzialmente
    for i in range(0,50):
        somma_arr[i]=arr[i]+arr2[i]     #inserisce in somma_arr la somma degli elementi di stesso indice degli altri due array
    
    return somma_arr

def sum_somma_arr():
    somma=np.sum(somma_arr)  #calcola la somma dell'array somma_arr
    return somma

def sum_magg_5():
    somma=np.sum(somma_arr[somma_arr>5])        #calcola la somma dell'array somma_arr con la condizione che gli elementi siano >5
    print(f"La somma degli elementi >5 sono: {somma}")
    return somma

#funzione stampa
def stampa():
    print(f"Array di 50 numeri equidistanti tra 0 e 1: {arr} ")
    print(f"Array di 50 numeri casuali tra 0 e 1: {arr2} ")
    print(f"Array somma elemento per elemento dei due array: {somma_arr} ")
    print(f"Somma totale del nuovo array: {somma} ")
    print(f"Somma degli elementi del nuovo array >5: {somma_mag_5} ")


def crea_array():       #crea array di 50 elementi equidistanti nel range acquisito in input
    while True:
        try:
            min=int(input("Inserisci il limite inferiore dell'array: "))
            break
        except:
            print("Errore nell'inserimento. Riprova")
    while True:
        try:
            max=int(input("Inserisci il limite superiore dell'array: "))
            if min!=max and max>min:
                break
            else:
                print("Il max deve essere superiore al min. Riprova")
        except:
            print("Errore nell'inserimento. Riprova")     
    arr=np.linspace(min,max,50) #creazione array
    return arr


def crea_array2():   #crea array di 50 numeri casuali tra 0 e 1
    arr2=np.random.rand(50)
    return arr2

def menu():
    print("""\n1. Crea array di 50 numeri equidistanti tra due limiti
2. Crea array di 50 numeri casuali tra 0 e 1
3. Somma elemento per elemento dei due array
4. Calcola la somma totale del nuovo array
5. Calcola la somma degli elementi del nuovo array >5
6. Stampa array originali, l'array somma e tutte le somme
0. ESCI
""")
    
contr_arr=False     #var di controllo
contr_arr2=False
contr_somma_arr=False 
contr_somma_mag=False  
contr_somma=False 
while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1": #Crea array di 50 numeri equidistanti tra due limiti 
        if contr_arr==False:
            arr=crea_array()
            print(f"L'array creato è: {arr}")
            contr_arr=True  #variabile di controllo. Se è false, non permetterà di operare sui numeri di un array (perché vuoto)
        else:       #se la var di controllo è già True, vuol dire che è già stato creato
            scelta=input("Array di 50 numeri equidistanti già creato. Vuoi modificare i limiti inferiori e/o superiori? ").lower()    #chiede se si vogliono modificare min e max
            if scelta=="si":
                arr=crea_array()    # se si, permette di creare il nuovo array con nuovi min e max
                print(f"L'array creato è: {arr}")

        contr_somma=False       #var di controllo della somma azzerati
        contr_somma_mag=False
        contr_somma_arr=False
    elif scelta=="2":   #2. Crea array di 50 numeri casuali tra 0 e 1
        if contr_arr2==False:
            arr2=crea_array2()
            print(f"L'array creato è: {arr2}")
            contr_arr2=True     #variabile di controllo. Se è false, non permetterà di operare sui numeri di un array (perché vuoto)
        else:
            print("Array di 50 numeri casuali tra 0 e 1 già creato.")

    elif scelta=="3":       #3. Somma elemento per elemento dei due array
        if contr_arr and contr_arr2 and contr_somma_arr==False:    #se i due array sono stati creati
            somma_arr=crea_array_somma()
            print(f"L'array creato è: {somma_arr}")
            contr_somma_arr=True    #variabile di controllo. Se è false, non permetterà di operare sui numeri di un array (perché vuoto)
        elif contr_somma_arr:
            print("Array somma già creato")
        elif contr_arr2==False or contr_arr==False:     #se le due var di controllo dei due array sono =False, permette di creare gli array
            if contr_arr2==False:
                scelta=input("Array di 50 numeri casuali tra 0 e 1 non creato. Vuoi crearlo? ").lower()
                if scelta=="si":
                    arr2=crea_array2()
                    contr_arr2=True
            if contr_arr==False:
                scelta=input("Array di 50 numeri equidistanti tra due valori non creato. Vuoi crearlo? ").lower()
                if scelta=="si":
                    arr=crea_array()
                    contr_arr=True
        else:
            print("Non tutti gli array sono stati creati")

    elif scelta=="4":   #4. Calcola la somma totale del nuovo array
        if contr_somma_arr:     #se l'array somma è già stato creato
            somma=sum_somma_arr()
            print(f"La somma totale del nuovo array è: {somma}")
            contr_somma=True
        else:
            print("Array somma non ancora creato")

    elif scelta=="5":       #5. Calcola la somma degli elementi del nuovo array >5
        if contr_somma_arr:
            somma_mag_5=sum_magg_5()
            contr_somma_mag=True    #var controllo =True
        else:
            print("Array somma non ancora creato")
    elif scelta=="6":   #6. Stampa array originali, l'array somma e tutte le somm
        if contr_arr and contr_arr2 and contr_somma_arr and contr_somma and contr_somma_mag:    #se le 3 var di controllo sono True, stampa()
            stampa()
        else:
            print("Alcuni array non sono stati creati ancora.")
            if contr_arr2==False or contr_arr==False: #se qualche var di controllo degli array o somme sono =False, permette di crearli o calcolarli
                if contr_arr2==False:   #creazione array di 50 numeri casuali tra 0 e 1
                    scelta=input("Array di 50 numeri casuali tra 0 e 1 non creato. Vuoi crearlo? ").lower()
                    if scelta=="si":
                        arr2=crea_array2()
                        contr_arr2=True
            if contr_arr==False:    #creazione Array di 50 numeri equidistanti tra due valori
                    scelta=input("Array di 50 numeri equidistanti tra due valori non creato. Vuoi crearlo? ").lower()
                    if scelta=="si":
                        arr=crea_array()
                        contr_arr=True
            if contr_somma_arr==False:  #creazione Array somma
                scelta=input("Array somma non creato. Vuoi crearlo? ").lower()
                if scelta=="si":
                    somma_arr=crea_array_somma()
                    contr_somma_arr=True
            if contr_somma==False:  #calcolo Somma dei due array
                scelta=input("Somma dei due array non ancora calcolata. Vuoi calcolarla? ").lower()
                if scelta=="si":
                    somma=sum_somma_arr()
                    print(f"La somma totale del nuovo array è: {somma}")
                    contr_somma=True       
            if contr_somma_mag==False:  #calcolo Somma degli elementi >5
                scelta=input("Somma degli elementi >5 dell'array \"somma_arr\" non ancora calcolata. Vuoi calcolarla? ").lower()
                if scelta=="si":
                    somma_mag_5=sum_magg_5()
                    contr_somma_mag=True 
            if contr_arr and contr_arr2 and contr_somma_arr and contr_somma and contr_somma_mag:    #se le 5 var di controllo ora sono True, stampa()
                print("Opzione ora disponibile:")
                stampa()                 
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")
print("CHIUSURA")