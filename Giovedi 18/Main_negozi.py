"""
Caricare i dati in un DataFrame.

Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.

Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.

Trovare il prodotto più venduto in termini di Quantità.

Identificare la città con il maggior volume di vendite totali.

Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).

Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.

Visualizzare il numero di vendite per ogni città.
"""
import ModNegozi as mod

df=mod.Vendite("Da Pino")

def menu():
    print("""\nMENU:
1. Aggiungi colonne Totale Vendite          
2. Raggruppa dati per Prodotto
3. Prodotto più venduto
4. Città con maggior volume di vendite totali
5. Visualizza nuovo frame con vendite superiori ad x
6. Ordina Totale vendite in ordine decrescente
7. Visualizza il numero di vendite per ogni città
0. Esci
""")

contr_tot=False
while True:
    menu()
    scelta=input("Inserisci una scelta: ")
    if scelta=="1":
        df.agg_tot_vendite()
        contr_tot=True
    elif scelta=="2":
        if contr_tot:       #CONTROLLA LA PRESENZA DELLA COLONNA TOTALE VENDITE
            df.group_df()
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla per poi vedere il totale vendite raggruppato? ").lower()
            if scelta=="si":        #se non c'è la colonna, si crea e poi si effettua l'opzione selezionata
                df.agg_tot_vendite()
                contr_tot=True
                df.group_df()
            else:
                print("Ritorno al menu.") 
        
    elif scelta=="3":
        df.prod_piu_vend()
    elif scelta=="4":
        if contr_tot:       #CONTROLLA LA PRESENZA DELLA COLONNA TOTALE VENDITE
            df.cit_vend_max()
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla prima di visualizza le città con le vendite massime? ").lower()
            if scelta=="si":        #se non c'è la colonna, si crea e poi si effettua l'opzione selezionata
                df.agg_tot_vendite()
                contr_tot=True
                df.cit_vend_max()
            else:
                print("Ritorno al menu.")
    elif scelta=="5":
        df.vend_sup_val()
    elif scelta=="6":
        if contr_tot:       #CONTROLLA LA PRESENZA DELLA COLONNA TOTALE VENDITE
            df.tot_vendite_dec()
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla per poi vederla ordinata in senso decrescente? ").lower()
            if scelta=="si":        #se non c'è la colonna, si crea e poi si effettua l'opzione selezionata
                df.agg_tot_vendite()
                contr_tot=True
                df.tot_vendite_dec()
            else:
                print("Ritorno al menu.")        
    elif scelta=="7":
        if contr_tot:       #CONTROLLA LA PRESENZA DELLA COLONNA TOTALE VENDITE
            df.vend_per_citta()
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla per poi vedere il numero di vendite per città? ").lower()
            if scelta=="si":    #se non c'è la colonna, si crea e poi si effettua l'opzione selezionata
                df.agg_tot_vendite()
                contr_tot=True
                df.vend_per_citta()
            else:
                print("Ritorno al menu.") 
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")

print("CHIUSURA")