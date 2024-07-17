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
import pandas as pd
import numpy as np

#LEGGE I DATI DAL CSV
def leggi_csv():
    df=pd.read_csv("5 settimana\\Mercoledi 17\\Pandas\\prodotti.csv")  #index_col=0 se il .csv ha la colonna indice alla prima colonna
    return df

#FUNZIONE PER CALCOLARE IL TOTALE VENDITE PER OGNI PRODOTTO
def agg_tot_vendite(df):
    df["Totale vendite"]=df["Quantita"]*df["Prezzo Unitario"]
    print("Colonna aggiunta correttamente")
    print(f"DataFrame aggiornato:\n{df}")

#FUNZIONE CHE RAGGRUPPA I DATI PER PRODOTTO
def group_df(df):
    df_ag = df.groupby("Prodotto").agg({        #"agg()" per effettuare la somma a quantità e totale vendita ma non prezzo unitario:
        "Quantita": "sum",
        "Totale vendite": "sum",
        "Prezzo Unitario": "first"  # Mantiene il primo valore di prezzo_unitario
    })
    print(f"\n---Valori raggruppati:---\n{df_ag}")

#funzine che calcola il prodotto più venduto
def prod_piu_vend(df):
    df_v=df.sort_values("Quantita")
    print(f"Il prodotto più venduto è:\n{df_v.tail(1)}")    #si trova in fondo, quindi è l'ultimo elemento

def cit_vend_max(df):
    df_v=df.sort_values("Totale vendite")   #ordina in senso crescente
    print(f"\n---La città che ha venduto di più venduto è:---\n{df_v.iloc[-1]["Citta"]}") #iloc per prendere un elemento all'indice indicato

#FUNZIONE PER VENDITE SUPERIORE AD UN VALORE X
def vend_sup_val(df):
    while True:
        try:
            val=int(input("Inserisci il valore del filtro: "))  #VALORE X
            break
        except:
            print("Valore non intero, riprova")
            
    df_v = df[df["Totale vendite"] > val]
    if len(df_v)>0:     #CONTROLLO CHE CI SIA ALMENO UN ELEMENTO > X
        print(f"Le righe con il \"Totale vendite\" > {val}:\n{df_v}")
    else:
        print("Nessuna vendita totale maggiore del valore che hai inserito")

#RAGGRUPPAMENTO VENDITE PER CITTA'
def vend_per_citta(df):
    df_c=df.groupby("Citta").agg({
        "Prezzo Unitario": "first",
        "Quantita": "sum",
        "Totale vendite": "sum", 
    })
    print(f"Le città raggruppate per vendite sono:\n{df_c}")

#FUNZIONE TOTALE VENDITE DECRESCENTE 
def tot_vendite_dec(df):
    df_tv=df.sort_values(by="Totale vendite",ascending = False)
    print(f"\n---ORDINE IN SENSO DECRESCENTE---\n{df_tv}")