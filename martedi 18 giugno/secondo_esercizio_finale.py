""" stringa="la sabbia è gialla"
print("la stringa è: "+ stringa +"\opzioni disponibili:")
print("Aggiungi\nRimuovi\nSostituisci")
selez=input("seleziona una tra le opzioni: ")
if(selez=="Aggiungi"):
    parola=input("Inserisci la parola da aggiungere: ")
    print(stringa +" "+ parola)
elif(selez=="Sostuisci"):
    parola_rim=input("Inserisci la parola da rimuovere: ")
    parola=input("Inserisci la parola da aggiungere: ")
    print(stringa.replace(parola_rim, parola))
else:
    #if(selez=="")
    parola=input("Inserisci la parola da rimuovere: ")
    print(stringa.replace(parola, "")) """

