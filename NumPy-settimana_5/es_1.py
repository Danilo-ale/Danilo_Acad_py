"""
utilizza la funzione np.arange per creare un array di interi
da 10 a 49

verifica il tipo di dato dell'array e stampa il risultato

cambia il tipo di dato dell'array in float 64 e verifica
il nuovo tipo di dato

stampa la forma dell'array
"""

import numpy as np



def menu():
    print("\nScegli:")
    print("1. Stampa il tipo di dato dell'array")
    print("2. Stampa array")
    print("3. Cambia il tipo di dato (da float64 a int64 e viceversa)")
    print("4. Stampa la forma dell'array")
    print("0. Esci")


def tipo_dato():
    print(f"il tipo di dato dell'array è: {arr.dtype}")

def stampa_array():
    print(arr)


def cambia_tipo_dato():
    if arr.dtype=="int64":
        arr.dtype="float64"
    else:
        arr.dtype="int64"
    
    print("Tipo di dato cambiato.")

def stampa_forma_array():
    print(f"Forma array: {arr.shape}")

while True:
    try:
        min=int(input("Inserisci il numero minimo dell'array: "))
        break
    except:
        print("Errore")

while True:
    try:
        max=int(input("Inserisci il numero massimo dell'array: "))
        break
    except:
        print("Errore")


arr=np.arange(min,max)

while True:
    menu()
    scelta=input("Scegli un'opzione: ")
    if scelta=="1":
        tipo_dato()
    elif scelta=="2":
        stampa_array()
    elif scelta=="3":
        cambia_tipo_dato()
    elif scelta=="4":
        stampa_forma_array()
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")

print("Chiusura programma")
    