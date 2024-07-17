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

df=mod.leggi_csv()
print(df) 
#mod.vend_per_citta(df)

def menu():
    print("""\nMENU:
1. Aggiungi colonne Totale Vendite          
2. Raggruppa dati per Prodotto
3. Prodotto più venduto
4. Città con maggior volume di vendite totali
5. Visualizza nuovo frame con vendite superiori ad x
6. Ordina Totale vendite in ordine decrescente
7. Viauslizza il numero di vendite per ogni città
0. Esci
""")

contr_tot=False
while True:
    menu()
    scelta=input("Inserisci una scelta: ")
    if scelta=="1":
        mod.agg_tot_vendite(df)
        contr_tot=True
    elif scelta=="2":
        if contr_tot:
            mod.group_df(df)
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla per poi vedere il totale vendite raggruppato? ").lower()
            if scelta=="si":
                mod.agg_tot_vendite(df)
                contr_tot=True
                mod.group_df(df)
            else:
                print("Ritorno al menu.") 
        
    elif scelta=="3":
        mod.prod_piu_vend(df)
    elif scelta=="4":
        if contr_tot:
            mod.cit_vend_max(df)
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla prima di visualizza le città con le vendite massime? ").lower()
            if scelta=="si":
                mod.agg_tot_vendite(df)
                contr_tot=True
                mod.cit_vend_max(df)
            else:
                print("Ritorno al menu.")
    elif scelta=="5":
        mod.vend_sup_val(df)
    elif scelta=="6":
        if contr_tot:
            mod.tot_vendite_dec(df)
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla per poi vederla ordinata in senso decrescente? ").lower()
            if scelta=="si":
                mod.agg_tot_vendite(df)
                contr_tot=True
                mod.tot_vendite_dec(df)
            else:
                print("Ritorno al menu.")        
    elif scelta=="7":
        if contr_tot:
            mod.vend_per_citta(df)
        else:
            scelta=input("Nel dataFrame non c'è ancora la tabella vendite totali. Vuoi crearla per poi vedere il numero di vendite per città? ").lower()
            if scelta=="si":
                mod.agg_tot_vendite(df)
                contr_tot=True
                mod.vend_per_citta(df)
            else:
                print("Ritorno al menu.") 
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")