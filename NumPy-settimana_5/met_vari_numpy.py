import numpy as np

arr=np.array([1,2,3,4,5])

#utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)
print(f"Dimensioni dell'array {arr.ndim}")
print(f"tipo di dati: {arr.dtype}")
print(f"NUmero di elementi: {arr.size}")
print(f"Somma degli elementi: {arr.sum()}")
print("Media degli elementi:", arr.mean())
print("Valore massimo:", arr.max())
print(f"Indice del valore massimo: {arr.argmax()}")


