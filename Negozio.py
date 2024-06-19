#vuoi iniziare il software?
controllo=True
lista_prod=["papera", "anello","gomma"]
lista_prez=[10,20,30]
lista_quant=[3,4,5]
acquisti_cliente=[]
guadagno=0
sel=input("Iniziare? ")
if(sel.lower()=="si"):
    while True:    
        scelta=input("Sei un cliente? ")
        if(scelta.lower()=="si"): 
            print("Benvenuto cliente")
            while True:
                print("Visualizzazione prodotti")
                print(lista_prod)
                sel_acq=input("Cosa vuoi acquistare? ")
                if sel_acq.lower() in lista_prod:
                    print("Prezzo di", sel_acq,":", lista_prez[lista_prod.index(sel_acq)])
                    dec_acq=input("Vuoi acquistare? ")
                    if dec_acq=="si":
                        print("Prodotto acquistato")
                        lista_quant[lista_prod.index(sel_acq)]-=1
                        acquisti_cliente.append(sel_acq)
                        guadagno+=lista_prez[lista_prod.index(sel_acq)]
                        print("Quantita aggiornate:")
                        print(lista_quant)
                        print("Acquisti cliente:", acquisti_cliente)
                        print("Guadagno: ", guadagno)
                    else:
                        pass
                else:
                    print("Prodotto non presente in lista")
                cont=input("vuoi continuare? ")
                if(cont.lower()=="no"):
                    print
                    break   

        elif(scelta.lower()=="no"):
            scelta2=input("Vuoi gestire l'inventario? ")
            if(scelta2.lower()=="si"):
                print("Benvenuto nell'inventario")
            elif(scelta2.lower()=="no"):
                scelta3=input("sei un amministratore? ")
                if(scelta3.lower()=="si"):
                    print("Benvenuto amministratore")
                else:
                    print("Chiusura")
                    break
    
else:
    print("Arrivederci")