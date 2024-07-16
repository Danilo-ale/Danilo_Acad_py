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
def crea_arr():
    arr=np.linspace(0,1,12)
    arr=arr.reshape(3,4)
    print(arr)
    return arr

def genera_matrice():
    arr=np.linspace(0,1,12).reshape(3,4)
    print(arr)
    return arr

arr1d=crea_arr()

mat=genera_matrice()
print(f"Somma dell'array: {np.sum(arr1d)}\nSomma della matrice: {np.sum(mat)}")
