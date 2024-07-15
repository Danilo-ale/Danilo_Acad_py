"""
utilizza la funzione np.arange per creare un array di interi
da 10 a 49

verifica il tipo di dato dell'array e stampa il risultato

cambia il tipo di dato dell'array in float 64 e verifica
il nuovo tipo di dato

stampa la forma dell'array
"""

import numpy as np


#stampa possibili operazioni
def menu():
    print("\nScegli:")
    print("1. Stampa il tipo di dato dell'array")
    print("2. Stampa array")
    print("3. Cambia il tipo di dato (da float64 a int64 e viceversa)")
    print("4. Stampa la forma dell'array")
    print("0. Esci")

#stampa il tipo di dato
def tipo_dato():
    print(f"il tipo di dato dell'array è: {arr.dtype}")
#stampa l'intero array
def stampa_array():
    print(arr)

#cambia il tipo di dato
def cambia_tipo_dato():
    if arr.dtype=="int64":
        arr.dtype="float64"
    else:
        arr.dtype="int64"
    
    print("Tipo di dato cambiato.")

#stampa la forma dell'array
def stampa_forma_array():
    print(f"Forma array: {arr.shape}")

#ciclo per acquisire il minimo dell'array
while True:
    try:
        min=int(input("Inserisci il numero minimo dell'array: "))
        break
    except:
        print("Errore")

#ciclo per acquisire il massimo dell'array
while True:
    try:
        max=int(input("Inserisci il numero massimo dell'array: "))
        break
    except:
        print("Errore")

#creazione array
arr=np.arange(min,max)

while True:
    menu()
    scelta=input("Scegli un'opzione: ")
    if scelta=="1": #Stampa il tipo di dato dell'array
        tipo_dato()
    elif scelta=="2":#Stampa array
        stampa_array()
    elif scelta=="3":   #Cambia il tipo di dato (da float64 a int64 e viceversa)
        cambia_tipo_dato()
    elif scelta=="4":   #Stampa la forma dell'array
        stampa_forma_array()
    elif scelta=="0":   #Esce dal while
        break
    else:
        print("Scelta sbagliata")

print("Chiusura programma")