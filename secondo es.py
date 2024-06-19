"""Andare a creare un if con vari elif e un else finale 
che gestisca un menu per la selezione di un crud basilare 
(aggiungi rimuovi elimina ) su una lista di stringhe"""

lista=["ciao"]
print(lista)
while (True):
    
    print("menù:")
    print("Aggiungi\nRimuovi\nSostituisci")
    selez=input("seleziona una tra le opzioni: ")
    if(selez=="Aggiungi"):
        parola=input("Inserisci la parola da aggiungere: ")
        lista.append(parola)
        print(lista)
    elif(selez=="Sostituisci"):
        parola_rim=input("Inserisci la parola da sostituire: ")
        parola=input("Inserisci la parola da aggiungere: ")
        if parola_rim in lista:
            print("ok")
            lista[lista.index(parola_rim)]= parola
            print(lista)

    elif(selez=="Rimuovi"):        
        parola=input("Inserisci la parola da rimuovere: ")
        if parola in lista:
            lista.remove(parola)
            print(lista)
    else:
        print("chiusura")
        break