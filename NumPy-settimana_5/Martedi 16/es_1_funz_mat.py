"""
Descrizione: Crea un array utilizzando linspace,
cambia la sua forma con reshape,
genera un array casuale e calcola la somma degli elementi.
Esercizio:
Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
Cambia la forma dell'array a una matrice 3x4.
Genera una matrice 3x4 di numeri casuali tra 0 e 1.
Calcola e stampa la somma degli elementi di entrambe le matrici.
"""

import numpy as np
#funzione crea array
def crea_arr():
    arr=np.linspace(0,1,12)
    arr=arr.reshape(3,4)
    print(arr)
    return arr

#funzione crea matrice
def genera_matrice():
    arr=np.linspace(0,1,12).reshape(3,4)
    print(arr)
    return arr

#menu
def menu():
    print("""1. Crea array
2. Crea la matrice
3. Calcola somma array
4. Calola somma matrice
0. Esci
""")
#variabili di controllo
contr_arr=False
contr_mat=False
while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        arr=crea_arr()
        contr_arr=True  #variabile di controllo. Se è false, non permetterà di sommare i numeri di un array (perché vuoto)
    elif scelta=="2":
        mat=genera_matrice()  #variabile di controllo. Se è false, non permetterà di sommare i numeri di una matrice (perché vuota)
        contr_mat=True
    elif scelta=="3":
        if contr_arr:
            print(f"Somma dell'array: {np.sum(arr)}")
        else:
            print("Array non ancora creato")
    elif scelta=="4":
        if contr_mat:
            print(f"Somma della matrice: {np.sum(mat)}")
        else:
            print("Matrice non ancora creata")
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")

print("Chisura")