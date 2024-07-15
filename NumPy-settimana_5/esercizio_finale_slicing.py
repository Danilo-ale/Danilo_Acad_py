import numpy as np
def crea_array():
    arr=np.random.randint(10,50,20)

    return arr

def stampa_primi_dieci_num():
    print(f"I primi 10 elementi sono: {arr[0:10]}")

def stampa_ultimi_cinque_num():
    print(f"Gli ultimi 5 elementi sono: {arr[-5:]}")

def stampa_range():
    print(f"Gli elementi dall'indice 5 all'indice 15 (escluso) sono: {arr[5:15]}")
    

def stampa_step():
    print(f"Elementi con step di 3: {arr[::3]}")

def modifica_elem():
    arr2=arr.copy()
    arr2[5:10]=99
    print(f"L'array modificato è: {arr2}")

def stampa_array_originale():
    print("array originale: ",arr)


arr=crea_array()
print(arr)

stampa_primi_dieci_num()
stampa_ultimi_cinque_num()
stampa_range()
stampa_step()
modifica_elem()
stampa_array_originale()