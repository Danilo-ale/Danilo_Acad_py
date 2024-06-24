"""
elenco di parole. per ogni parola scrivere la lunghezza
"""
while True:
    stringa=input("Inserisci stringa: ")


    lista=stringa.split(" ")
    for parola in lista:
        #print('La lunghezza di"', parola, '"è:', len(parola))
        print(f'La lunghezza di" {parola}" è:{len(parola)}')
    scelta=input("Continuare? ").lower()
    if scelta!="si":
        break
    


