import analisi_dati_df as mod
df=mod.crea_df()

while True:
    mod.menu()
    scelta=input("Inserisci una scelta: ")
    if scelta=="1": #1. Visualizza le prime cinque righe del dataframe
        mod.visualizza_prime_righe(df)  
    elif scelta=="2":   #2. Visualizza le ultime cinque righe del dataframe
        mod.visualizza_ultime_righe(df)
    elif scelta=="3":   #3. Visualizza il tipo di dati di ciascuna colonna
        mod.tipo_dati(df)
    elif scelta=="4":   #4. Calcola media, mediana e deviazione standard
        mod.calcola_stat(df)    
    elif scelta=="5":   #5. Rimuovi duplicati
        mod.elimina_dupl(df)
    elif scelta=="6":   #6. Gestisci valori mediani
        mod.gestisci_val(df)
    elif scelta=="7":   #7. Aggiungi categoria età
        mod.agg_cat_eta(df)
        print(df)   
    elif scelta=="8":   #8. Salva in file.csv
        mod.salva_csv(df)
    elif scelta=="9":   #9. Visualizza dataframe
        print(df)
    elif scelta=="0":   #0. Esci
        break
    else:
        print("Scelta sbagliata")

print("CHIUSURA PROGRAMMA")