"""
richiedere 3 valori: nome, anno di nascita, giorno della settimana in numero
dopo il programma stampa "Il tuo nome è:" , "Hai anni: ", "Mancano tot giorni a sabato"
"""
from datetime import datetime

data = datetime.now()
while True:
    while True:
        nome=input("Inserisci il tuo nome: ")
        if(nome.isnumeric()):
            print("Inserisci un nome valido")
        else:
            break

    while True:
        nasc=int(input("Inserisci l'anno di nascita: "))
        if(nasc>1910 and nasc<data.year):
            break
        else:
            print("Inserisci un anno di nascita corretto")
    while True:
        giorno=int(input("Inserisci il giorno in numeri: "))
        if(giorno>0 and giorno <8):
            break
        else:
            print("Inserisci un giorno corretto")
    sab=6
    print("Il tuo nome è:",nome)

    print(f"Hai {data.year-nasc} anni")

    if(giorno>sab):
        print(f"Mancano {sab*2-giorno+1} giorni a sabato")
    else:
        print(f"Mancano {sab-giorno} giorni a sabato")
    scelta=input("Continuare? ").lower()
    if scelta!="si":
        break