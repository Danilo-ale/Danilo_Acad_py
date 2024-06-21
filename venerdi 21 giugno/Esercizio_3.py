while True:
    num=input("inserisci numero max: ")
    step=input("Inserisci lo step: ")
    if(num.isnumeric() and step.isnumeric()):  #controllo input
        numeri=[*range(0,int(num),int(step))]   #creazione range
        for num in numeri:      #stampa numeri
            print(num)
    else:
        print("Numero max o step o entrambi non sono numeri.")

    scelta=input("continuare? ").lower() #scelta per continuare nel while
    if(scelta!="si"):
        break
print("Arrivederci")    