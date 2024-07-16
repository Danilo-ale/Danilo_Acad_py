"""
Consegna:

1.Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali 
compresi tra 1 e 100.
2.Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
3.Inverti le righe della matrice estratta 
(cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
4.Estrai la diagonale principale della matrice invertita e crea un array 1D contenente 
questi elementi.
5.Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3
 con il valore -1.
6.Stampa la matrice originale, la sotto-matrice centrale estratta,
 la matrice invertita, la diagonale principale e la matrice invertita modificata.


Obiettivo:

Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, 
modificare e manipolare sotto-matrici e array, applicando operazioni avanzate 
come l'inversione delle righe e la sostituzione condizionale degli elementi.
"""

import numpy as np

arr2d=np.random.randint(1,101,36).reshape(6,6)
print(f"Matrice:\n {arr2d}")
def sottomatrice():
    print(f"sotto matrice dell'array:\n {arr2d[1:5,1:5]}")

def inverti_righe():
    lista_c=[]
    i=0
    j=5
    while i<j:
        lista_c=arr2d[i].copy()
        arr2d[i]=arr2d[j]
        arr2d[j]=lista_c
        i+=1
        j=j-1
    
    print(f"Matrice invertita:\n{arr2d}")

def diag_principale():
    diagonale=arr2d.diagonal()
    print(f"La diagonale della matrice invertita è: {diagonale}")

def sost_elem():
    i=0
    for i in range(0,6):
        for j in range(0,6):
            if arr2d[i][j]%3==0:
                arr2d[i][j]=-1

    print("Matrice è:\n",arr2d)

print("Matrice: ",arr2d)
sottomatrice()
inverti_righe()
diag_principale()
sost_elem()