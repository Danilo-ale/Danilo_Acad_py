"""
Esercizio 1: Somma e Media di Elementi

Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.

Calcolare e stampare la somma di tutti gli elementi dell'array.

Calcolare e stampare la media di tutti gli elementi dell'array.
"""

import numpy as np

v=np.random.randint(1,100,size=15)

def menu():
    print("""\n1. Crea vettore
2. Calcola la somma
3. Calcola la media
0. Esci
""")
    
def crea_v():
    while True:
        try:
            min=int(input("Inserisci il minimo del vettore: "))
            break
        except:
            print("Errore")
    while True:
        try:
            max=int(input("Inserisci il massimo del vettore: "))
            if max>min:
                break
            else:
                print(f"Il massimo deve essere superiore al minimo ({min})")
        except:
            print("Errore")
    v=np.random.randint(min,max,size=15)
    return v

def somma_v():
    print(f"La somma del vettore è: {np.sum(v)}")

def media_v():
    print(f"La media del vettore è: {np.mean(v)}")

contr_v=False
while True:
    menu()
    scelta=input("Inserisci una scelta: ")
    if scelta=="1":
        v=crea_v() 
        contr_v=True
    elif scelta=="2":
        if contr_v:
            somma_v()
    elif scelta=="3":
        if contr_v:
            media_v()
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")

print("Chiusura")