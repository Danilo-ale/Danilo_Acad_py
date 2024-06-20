
lista_prod=["papera", "anello","gomma"]   #lista prodotti 
lista_prez=[10,20,30]   #lista prezzi
lista_quant=[0,4,5] #lista quantità
acquisti_cliente=[] #lista acquisti cliente

lista_log=["pino", "ciccio"]
lista_pas_log=["123", "45"]
guadagno=0   #guadagno venditore
sel=input("Iniziare? ")   #chiede se si vuole far iniziare il software
if(sel.lower()=="si"):  #se si, inizia
    while True:    #ripete sempre se si è un cliente, se si vuole gst inventario o se si vuole amministrare
        scelta=input("Sei un cliente? ")   #chiede se si è un cliente
        if(scelta.lower()=="si"):   #se si è un cliente
            print("Benvenuto cliente")
            while True:     #ripete fino a quando si vuole acquistare
                print("Visualizzazione prodotti")
                for item in lista_prod:  #visualizza i prodotti con quantità
                    print(item, "Quantità: ", lista_quant[lista_prod.index(item)])
                sel_acq=input("Cosa vuoi acquistare? ")  #si chiede al cliente cosa si vuole acquistare
                if sel_acq.lower() in lista_prod and lista_quant[lista_prod.index(sel_acq)]:   #se il prodotto selezionato è nella lista dei prodotti..
                    print("Prezzo di", sel_acq,":", lista_prez[lista_prod.index(sel_acq)])   #... visualizza il prezzo del prodotto
                    dec_acq=input("Vuoi acquistare? ")   #chiede se si vuole acquistare
                    if dec_acq=="si":   #se si...
                        print("Prodotto acquistato")  #... visualizza un messaggio di conferma di prodotto acquistato
                        lista_quant[lista_prod.index(sel_acq)]-=1  #decrementa le quantità del prodotto acquistato
                        acquisti_cliente.append(sel_acq)  #inserisce nella lista acquisti del cliente il prodotto acquistato
                        guadagno+=lista_prez[lista_prod.index(sel_acq)] #aumenta il valore della variabile guadagno
                        print("Quantita aggiornate:")  #visualizza le quantità aggiornate
                        print(lista_quant)
                        print("Acquisti cliente:", acquisti_cliente) #visualizza la lista degli acquisti del cliente
                        print("Guadagno: ", guadagno) #visualizza il guadagno (per una prova di funzionamento)
                    else:
                        pass   #se non si vuole acquistare dopo aver visto il prezzo, continua avanti
                else:
                    print("Prodotto non presente in lista o quantità terminate") #se il prodotto digitato non è nella lista, lo segnala in output
                cont=input("vuoi continuare? ")   #si chiede se si vuole continuare con l'acquisto
                if(cont.lower()=="no"):  #se no...
                    break   #...esce

        elif(scelta.lower()=="no"):   #se non si è un cliente
            scelta2=input("Vuoi gestire l'inventario? ")   #... si chiede se si vuole gestire un inventario
            if(scelta2.lower()=="si"): #se si vuole gestire l'inventario...
                print("Benvenuto nell'inventario")   #dà un messaggio di benvenuto
                while True:  #si ripetono le azioni fino a quando si vuole gestire l'inventario
                    print("Visualizzazione inventario: ")   
                    for prod in lista_prod:   #visualizza per ogni prodotto anche il prezzo e la quantità
                        print(prod, "Quantità: ", lista_quant[lista_prod.index(prod)], "prezzo: ", lista_prez[lista_prod.index(prod)])
                    print("Menù:")  #visualizzazione menù
                    print("1. Aggiungi articolo")
                    print("2. Rimuovi articolo")
                    print("3. Aggiorna articolo")
                    scelta_inv=input("Scegli una delle opzioni: ")   #scelta menù
                    if(scelta_inv=="1"):   # se si vuole aggiungere un articolo...
                        art_agg=input("Nome articolo? ")  #...si chiedono i dettagli del nuovo articolo
                        quant_agg=input("Quantità articolo? ")
                        prezzo_agg=input("Prezzo articolo? ")
                        lista_prod.append(art_agg)  #si aggiornano le liste con i nuovi dati
                        lista_quant.append(quant_agg)
                        lista_prez.append(prezzo_agg)
                        print("Inventario aggiornato:")  #visualizzazione inventario aggiornato
                        print(lista_prod)
                        print(lista_quant)
                        print(lista_prez)
                    elif(scelta_inv=="2"):   #se si vuole rimuovere un articolo...
                        for prod in lista_prod:   #...si visualizzano tutti i prodotti in inventario
                            print(prod)
                        art_rim=input("Scrivi l'articolo da rimuovere: ") #si seleziona l'articolo da rimuovere
                        if art_rim in lista_prod:   #se il prodotto è presente nella lista
                            
                            lista_quant.pop(lista_prod.index(art_rim))   #si eliminano tutti le informazioni correlate (prezzo, quantità) dell'articolo
                            lista_prez.pop(lista_prod.index(art_rim))
                            lista_prod.remove(art_rim)
                            print("Inventario aggiornato:") #visualizzazione inventario aggiornato
                            print(lista_prod)
                            print(lista_quant)
                            print(lista_prez)
                        else:
                            print("Articolo non presente") #se non è nella lista, output errore
                    elif(scelta_inv=="3"):   #se si vuole aggiornare l'inventario
                        art_aggior=input("Scegli l'articolo da aggiornare: ")   #si sceglie l'articolo da aggiornare
                        if art_aggior in lista_prod:    # se è presente nella lista, si visualizzano sotto i dettagli del prodotto scelto
                            print(art_aggior, "Quantità: ", lista_quant[lista_prod.index(art_aggior)], "prezzo: ", lista_prez[lista_prod.index(art_aggior)])
                            dett_aggior=input("Cosa vuoi aggiornare del prodotto? ")   #si chiede cosa si vuole aggiornare
                            if dett_aggior.lower()=="prezzo":   #se si vuole aggiornare il prezzo...
                                pr_aggior=input("Inserisci il nuovo prezzo: ")  #... si chiede il nuovo prezzo
                                lista_prez[lista_prod.index(art_aggior)]=pr_aggior    #si aggiorna la lista_prezzo con il nuovo prezzo
                                print("Prezzo aggiornato: ",lista_prez[lista_prod.index(art_aggior)])  #si visualizza il prezzo aggiornato
                            elif dett_aggior.lower()=="nome":   #se si vuole aggiornare il nome...
                                nome_aggior=input("Inserisci il nuovo nome del prodotto: ")   #... si chiede il nome dell'articolo
                                lista_prod[lista_prod.index(art_aggior)]=nome_aggior   #si aggiorna il nome del prodotto
                                print("Visualizzazione articolo aggiornato: ")
                                print(nome_aggior, "Quantità: ", lista_quant[lista_prod.index(nome_aggior)], "prezzo: ", lista_prez[lista_prod.index(nome_aggior)])
                            elif dett_aggior.lower()=="quantità":   #se si vuole aggiornare la quantità...
                                quant_agg=input("Inserisci la quantità da aggiornare: ")   #...si chiede la nuova quantità da aggiornare
                                lista_quant[lista_prod.index(art_aggior)]=quant_agg   #si aggiorna la quantità
                                print("Visualizzazione articolo aggiornato: ")  #si visualizzano i dettagli dell'articolo con le informazioni aggiornate
                                print(art_aggior, "Quantità: ", lista_quant[lista_prod.index(art_aggior)], "prezzo: ", lista_prez[lista_prod.index(art_aggior)])

                            else:   #se l'utente non digita cosa vuole modificare in maniera corretta
                                print("Selezione sbagliata")
                        else:   # se digita un articolo non presente nella lista
                             print("articolo non presente")
                    else:    #se non sceglie tra le opzioni disponibili dell'inventario
                        print("Comando sbagliato")

                    #si chiede se si vuole continuare
                    cont=input("Continuare? ")
                    if cont=="no":
                        break
                    
            elif(scelta2.lower()=="no"):
                scelta3=input("sei un amministratore? ")
                if(scelta3.lower()=="si"):
                    nome=input("Inserisci nome amministratore: ")    #verifica credenziali
                    passw=input("Inserisci password amministratore: ")
                    if nome in lista_log: 
                        if passw==lista_pas_log[lista_log.index(nome)]:   #se nome utente e pass coincidono visualizza il menù
                            while True:
                                print("Benvenuto amministratore")
                                print("Visualizzazione menù:")
                                print("1. Visualizza rapporto vendite")
                                print("2. Visualizza lo stato corrente dell'inventario")
                                print("3. Visualizza i guadagni totali")
                                selez=input("Seleziona una delle opzioni: ")
                                if selez=="1":
                                    print("Visualizzazione oggetti venduti: ")   #visualizza il rapport vendite
                                    print(acquisti_cliente)
                                elif selez=="2":
                                    print("Visualizzazione inventario: ")   #visualizza prod e quantità per ogni elemento
                                    for item in lista_prod:
                                        print(item, ", quantità:", lista_quant[lista_prod.index(item)])
                                elif selez=="3":    #visualizza i guadagni totali
                                    print("Guadagni totali:", guadagno)
                                else:       #se ha sbagliato a scegliere tra le opzioni, visualizza errore
                                    print("selezione sbagliata")   
                                contin=input("Continuare? ")
                                if contin.lower()=="no":
                                    break

                    else:
                        print("Nome utente sbagliato")  #se il nome utente non trova corrispondenza nella lista, visualizza errore

                else:
                    print("Chiusura")  #se non è un cliente, nè gestore inventario nè amministratore, chiude
                    break
    
else:
    print("Arrivederci")