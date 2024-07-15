"""
utilizza la funzione np.arange per creare un array di interi
da 10 a 49

verifica il tipo di dato dell'array e stampa il risultato

cambia il tipo di dato dell'array in float 64 e verifica
il nuovo tipo di dato

stampa la forma dell'array
"""

import numpy as np

#1.
arr=np.arange(10,50)
print(arr)

#2.
print(f"il tipo di dato dell'array è: {arr.dtype}")

#3.
arr.dtype="float64"

print(f"il nuovo tipo di dato dell'array è: {arr.dtype}")
print(arr.shape)
