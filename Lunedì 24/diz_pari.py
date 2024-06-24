"""
Scrivete un programma che chiede un numero all’utente e
restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }
"""

numero={}
numero.setdefault("Quadrato")
numero.setdefault("Pari o dispari")
numero.setdefault("n. cifre")

print(numero)
while True:
    num=input("Inserisci numero: ")
    if num.isdigit():
        num
        break
    else:
        print("Valore non valido. Riprova \n")
num=int(num)
numero["Quadrato"]=num**2
if num%2==0:
    numero["Pari o dispari"]="Pari"
else:
    numero["Pari o dispari"]="Dispari"

num=str(num)
numero["n. cifre"]=len(num)
    

print(numero)


print(num)