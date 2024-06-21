while True:
    stringa=input("Inserisci una stringa: ")  #inserimento stringa
    for let in stringa:
        print(let)      # per ogni lettera, la stampo
    scelta=input("continuare? ").lower() #scelta per continuare nel while
    if(scelta!="si"):
        break
print("Arrivederci")