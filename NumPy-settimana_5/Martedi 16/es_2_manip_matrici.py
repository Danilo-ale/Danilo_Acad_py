"""
Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale 
della matrice.
"""
import numpy as np

def menu():
    print("""\n1. Crea vettore
2. Estrarre e stampare la seconda colonna della matrice
3. Estrarre e stampare la terza riga della matrice
4. Calcolare la somma degli elementi della diagonale principale
0. Esci
""")

contr_v=False
while True:
    menu()
    scelta=input("Inserisci una scelta: ")
    if scelta=="1": #Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
        v=np.arange(1,25+1).reshape(5,5) 
        print(v)
        contr_v=True
    elif scelta=="2":   #Estrarre e stampare la seconda colonna della matrice.
        if contr_v:
            print("Seconda colonna della matrice:",v[:,1])

    elif scelta=="3":   #Estrarre e stampare la terza riga della matrice
        if contr_v:
            print("Terza riga della matrice:",v[2])
    elif scelta=="4":   #Calcolare e stampare la somma degli elementi della diagonale principale
        if contr_v:
            diagonale=v.diagonal()
            print(f"La diagonale è: {diagonale}, la sua somma è: {np.sum(diagonale)}")
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")