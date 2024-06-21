
while True:
    
    lista_pari=[]
    lista_dis=[]                                    #liste vuote
    min=int(input("Inserisci il min: "))        #inserimento numeri
    max=int(input("inserisci il max: "))
    numeri=[*range(min,max+1)]                      #creazione sequenza numeri
    for i in numeri:
        if(i%2==0):                                 #inserimento num dispari e pari nelle rispettive liste
            lista_pari.append(i)
        else:
            lista_dis.append(i)
    print(lista_pari)
    print(lista_dis)
    while True:
        print("menù")               #menu
        print("1. Visualizza pari")
        print("2. Visualizza dispari")
        print("3. Visualizza l'intera lista")
        selez=input("Scegli tra le opzioni")
        if selez=="1":                              #se seleziona pari, stampa i pari
            print("Numeri pari: ")
            for i in lista_pari:
                print(i)
        elif selez=="2":
            print("Numeri dispari: ")       #se seleziona dispari, stampa i dispari
            for i in lista_dis:
                print(i)
        elif selez=="3":                    #stampa tutti i numeri
            print("Tutti i numeri:")
            for i in numeri:
                print(i)
        else:
            print("selezione sbagliata.")
        selez=input("Vuoi continuare con questi numeri? ")      #rivisualizza il menu in caso l'utente voglia continuare con gli stessi numeri
        if selez.lower()!="si":
            break
    selez=input("Continuare con la seconda opzione? ")
    if selez.lower()!="si":
            break