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

arr2d=np.random.randint(1,101,size=(6,6))
print(f"Matrice:\n {arr2d}")
#funzione che stampa la sottomatrice 4x4
def sottomatrice():
    print(f"La sotto matrice 4x4 dell'array è:\n {arr2d[1:5,1:5]}")

#funzione che inverte le righe
def inverti_righe():
    mat=arr2d.copy()
    lista_c=[]      #lista di comodo
    i=0
    j=5
    while i<j:      #inverte le righe
        lista_c=mat[i].copy()
        mat[i]=mat[j]
        mat[j]=lista_c
        i+=1
        j=j-1
    
    return mat

#funzione diagonale principale
def diag_principale():
    mat=inverti_righe()
    diagonale=mat.diagonal()
    print(f"La diagonale della matrice invertita è: {diagonale}")

#funzione sostituisce gli elementi multipli di 3 con -1
def sost_elem():
    mat=inverti_righe()
    i=0
    for i in range(0,6):
        for j in range(0,6):
            if mat[i][j]%3==0:
                mat[i][j]=-1

    print("Matrice con gli elementi sostituiti è:\n",mat)

#richiama tutte le altre funzioni
def stampa():
    print(f"La matrice originale è: {arr2d}")
    sottomatrice()
    inverti_righe()
    diag_principale()
    sost_elem()

#menu
def menu():
    print("""\n1.Estrai sottomatrice 4x4
2. Inverti righe della matrice
3. Estrai la diagonale principale della matrice invertita
4. Sostituisci i multipli di 3 con -1
5. Stampa ogni operazione
0. Esci
""")

while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1": #1.Estrai sottomatrice 4x4
        sottomatrice()
    elif scelta=="2":   #2. Inverti righe della matrice
        mat_inv=inverti_righe()
        print(f"Matrice invertita:\n{mat_inv}")

    elif scelta=="3":   #3. Estrai la diagonale principale della matrice invertita
        diag_principale()
    elif scelta=="4":    #4. Sostituisci i multipli di 3 con -1
        sost_elem()
    elif scelta=="5":   #5. Stampa ogni operazione
        stampa()
    elif scelta=="0":   #0. Esci
        break
    else:
        print("Scelta sbagliata")

print("CHIUSURA PROGRAMMA")