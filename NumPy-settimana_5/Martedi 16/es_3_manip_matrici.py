"""
Esercizio 3: Operazioni con Fancy Indexing

Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.

Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici
 (0, 1), (1, 3), (2, 2) e (3, 0).

Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
 dell'array (considerando la numerazione delle righe che parte da 0).

Modificare gli elementi selezionati nel primo punto dell'esercizio 
aggiungendo 10 al loro valore.
"""


import numpy as np
#selezionare e stampare gli elementi agli indici  (0, 1), (1, 3), (2, 2) e (3, 0).
def stampa_elem_indici():
    indice=[[0,1],[1,3],[2,2],[3,0]]
    print("Stampa degli elementi negli indici (0, 1), (1, 3), (2, 2) e (3, 0): ")
    for i in indice:
        print(f"\nValore: {v[i[0]][i[1]]}", end="")

#selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).

def stampa_righe_disp():
    indice2=[*range(0,v.shape[0])]
    for i in indice2:
        if i%2==1:
            print("Posizione",i ,":",v[i])

#Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
def modifica_elem_indici():
    indice=[[0,1],[1,3],[2,2],[3,0]]
    print("Modifica degli elementi negli indici (0, 1), (1, 3), (2, 2) e (3, 0): ")
    for i in indice:
        print(f"Valore: {v[i[0]][i[1]]} ", end="")
        v[i[0]][i[1]]+=10
        print(f"Ora modificato in: {v[i[0]][i[1]]}")    
#menu
def menu():
    print("""\n1. Crea vettore
2. stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0)
3. stampare tutte le righe dispari
4. Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
0. Esci
""")

contr_v=False
while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1": #Creare vettore
        v=np.random.randint(10,50,size=16)
        v=v.reshape((4,4))
        print(v)
        contr_v=True
    elif scelta=="2":   #stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0)
        if contr_v:
            stampa_elem_indici()
        else:
            print("Vettore non ancora creato")
    elif scelta=="3":   #selezionare e stampare tutte le righe dispari dell'array
        if contr_v:
            stampa_righe_disp()
        else:
            print("Vettore non ancora creato")
    elif scelta=="4":   #Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
        if contr_v:
            modifica_elem_indici()
        else:
            print("Vettore non ancora creato")
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")