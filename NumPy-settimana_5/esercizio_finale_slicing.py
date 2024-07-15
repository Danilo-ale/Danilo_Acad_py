import numpy as np
def crea_array():
    arr=np.random.randint(10,50,20)

    return arr

#funzioni 
def stampa_primi_dieci_num():
    print(f"I primi 10 elementi sono: {arr[0:10]}")

def stampa_ultimi_cinque_num():
    print(f"Gli ultimi 5 elementi sono: {arr[-5:]}")

def stampa_range():
    print(f"Gli elementi dall'indice 5 all'indice 15 (escluso) sono: {arr[5:15]}")
    
def stampa_step():
    print(f"Elementi con step di 3: {arr[::3]}")

def modifica_elem():
    arr2=arr.copy() #copia nell'array2 gli elementi dell'array 
    arr2[5:10]=99   #assegna 99 dal quinto al decimo indice
    print(f"L'array modificato è: {arr2}")

def stampa_array_originale():
    print("array originale: ",arr)

#creazione array
arr=crea_array()
print(arr)

#menu
def menu():
    print("""\nOPZIONI:
1. Stampa i primi 10 numeri
2. Stampa gli ultimi 5 numeri
3. Stampa numeri dall'indice 5 al 15 escluso
4. Stampa i numeri con step di 3
5. Modifica gli elementi dall'indice 5 al 10
6. Stampa array originale
0. Esci
""")
    

while True:
    menu()
    scelta=input("Scegli un'opzione: ")
    if scelta=="1":     #1. Stampa i primi 10 numeri
        stampa_primi_dieci_num()
    elif scelta=="2":   #2. Stampa gli ultimi 5 numeri
        stampa_ultimi_cinque_num()
    elif scelta=="3":   #3. Stampa numeri dall'indice 5 al 15 escluso
        stampa_range()
    elif scelta=="4":   #4. Stampa i numeri con step di 3
        stampa_step()
    elif scelta=="5":   #5. Modifica gli elementi dall'indice 5 al 10
        modifica_elem()
    elif scelta=="6":   #6. Stampa array originale
        stampa_array_originale()
    elif scelta=="0":   #Esce dal while
        break
    else:
        print("Scelta sbagliata")

