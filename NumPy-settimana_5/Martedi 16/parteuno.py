"""
Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 

Il programma deve presentare un menu interattivo che consente all'utente
 di eseguire varie operazioni sulla matrice. Le operazioni disponibili includono:

Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma.
"""
import numpy as np
def menu():
    pass

def crea_matrice():
    while True:
        try:
            righe=int(input("Inserisci il numero di righe: "))
            break
        except:
            print("Errore. Riprova")
    while True:
        try:
            col=int(input("Inserisci il numero di colonne: "))
            break
        except:
            print("Errore. Riprova")

    matrice = np.random.randint(0,100,size=(righe,col))
    print(matrice)
    return matrice,righe,col

def sotto_matrice(matrice,righe,col):
    print(f"Sotto matrice centrale:\n {matrice[1:righe-1,1:col-1]}")

def trasp_matrice(matrice):
    matr=matrice.T
    print(matr)

def somma_elem(matrice):
    print(f"La somma della matrice è: {np.sum(matrice)}")

"""mat,righe,col=crea_matrice()
#sotto_matrice(mat,righe,col)
trasp_matrice(mat)
somma_elem(mat)"""