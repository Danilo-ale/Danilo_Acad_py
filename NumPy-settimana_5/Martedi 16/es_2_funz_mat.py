"""Consegna:

1.Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2.Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
3.Somma i due array elemento per elemento per ottenere un nuovo array.
4.Calcola la somma totale degli elementi del nuovo array.
5.Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6.Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
"""
import numpy as np

def crea_array_somma():
    somma_arr=np.zeros(10)
    for i in range(0,10):
        somma_arr[i]=arr[i]+arr2[i]
    
    return somma_arr

def sum_somma_arr():
    somma=np.sum(somma_arr)
    return somma

def sum_magg_5():
    somma=np.sum(somma_arr[somma_arr>5])
    print(f"La somma degli elementi >5 sono: {somma}")
    return somma

def stampa():
    print(f"Array di 50 numeri equidistanti tra 0 e 1: {arr} ")
    print(f"Array di 50 numeri casuali tra 0 e 1: {arr2} ")
    print(f"Array somma elemento per elemento dei due array: {somma_arr} ")
    print(f"Somma totale del nuovo array: {somma} ")
    print(f"Somma degli elementi del nuovo array >5: {somma_mag_5} ")
    


def crea_array():
    arr=np.linspace(0,1,10)
    return arr

def crea_array2():
    arr2=np.random.rand(10)
    return arr2

def menu():
    print("""\n1.Crea array di 50 numeri equidistanti tra 0 e 1
2. Crea array di 50 numeri casuali tra 0 e 1
3. Somma elemento per elemento dei due array
4. Calcola la somma totale del nuovo array
5. Calcola la somma degli elementi del nuovo array >5
6. Stampa array originali, l'array somma e tutte le somme
0. ESCI
""")
    
contr_arr=False
contr_arr2=False
contr_somma_arr=False    
while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        arr=crea_array()
        print(f"L'array creato è: {arr}")
        contr_arr=True
    elif scelta=="2":
        arr2=crea_array2()
        print(f"L'array creato è: {arr2}")
        contr_arr2=True
    elif scelta=="3":
        if contr_arr and contr_arr2:
            somma_arr=crea_array_somma()
            print(f"L'array creato è: {somma_arr}")
            contr_somma_arr=True
        else:
            print("Non tutti gli array sono stati creati")
    elif scelta=="4":
        if contr_somma_arr:
            somma=sum_somma_arr()
            print(f"La somma totale del nuovo array è: {somma}")

        else:
            print("Array somma non ancora creato")
    elif scelta=="5":
        if contr_somma_arr:
            somma_mag_5=sum_magg_5()
        else:
            print("Array somma non ancora creato")
    elif scelta=="6":
        if contr_arr and contr_arr2 and contr_somma_arr:
            stampa()
        else:
            print("Alcuni array non sono stati creati ancora.")
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")

print("CHIUSURA")