"""
Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 

Caricare i dati in un DataFrame autogenerandoli casualmente .

Visualizzare le prime e le ultime cinque righe del DataFrame.

Visualizzare il tipo di dati di ciascuna colonna.

Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).

Identificare e rimuovere eventuali duplicati.

Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.

Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).

Salvare il DataFrame pulito in un nuovo file CSV.
"""
import pandas as pd
import numpy as np
from random import choice
#MENU
def menu():
    print("""\NMENU:
1. Visualizza le prime cinque righe del dataframe
2. Visualizza le ultime cinque righe del dataframe
3. Visualizza il tipo di dati di ciascuna colonna
4. Calcola media, mediana e deviazione standard
5. Rimuovi duplicati
6. Gestisci valori mediani
7. Aggiungi categoria età
8. Salva in file.csv
9. Visualizza dataframe          
0. Esci
""")
#FUNZIONE CHE SOSTITUISCE I VALORI MANCANTI DI ETA E SALARIO CON I VALORI MEDI
def gestisci_val(df):
    df.fillna({"eta": df["eta"].mean()}, inplace=True)
    df.fillna({"salario": df["salario"].mean()}, inplace=True)
    
    print(df)
    return df

#SALVA IL DF SU UN FILE.CSV
def salva_csv(df):
    try:
        df.to_csv("5 settimana\\Mercoledi 17\\Pandas\\dataset_persone.csv")
        print("Salvataggio avvenuto correttamente")
    except:
        print("Errore nel salvataggio")
    
#FUNZIONE CHE RITORNA LA CATEGORIA DI ETA DI OGNI PERSONA
def cat_eta(eta):
    if eta < 18:
        return "Giovane"
    elif eta < 65 and eta >=18:
        return "Adulto"
    elif eta>=65:
        return "Senior"
    else:
        return "Errore"
#FUNZIONE CHE AGGIUNGE LA CATEGORIA ETA
def agg_cat_eta(df):
    df["Categoria eta"]=df["eta"].apply(cat_eta)

#FUNZIONE PRINT DEL TIPO DEI DATI DELLE COLONNE
def tipo_dati(df):
    print(f"Il tipo di dati del dataframe è: {df.dtypes}")

#FUNZIONE CHE VISUALIZZA LE PRIME 5 RIGHE
def visualizza_prime_righe(df):
    print(f"Le prime cinque righe sono:\n {df.head()}")

#FUNZIONE CHE VISUALIZZA LE ULTIME 5 RIGHE
def visualizza_ultime_righe(df):
    print(f"Le ultime cinque righe sono:\n {df.tail()}")

#FUNZIONE CHE CALCOLA LE STATISTICHE
def calcola_stat(df):
    statistiche=df.describe()   #describe ritorna una descrizione di tutte le statistiche, ma ce ne servono solo 3
    statistiche_cl=statistiche.loc[["mean","std","50%"]]    #loc per selezionare specifiche righe del df "statistiche "che contiene le statistiche
    statistiche_cl=round(statistiche_cl,2)     #arrotonda le cifre decimali a 2
    statistiche_cl.rename(index={"50%":"Mediana"}, inplace=True)    #rinomina i valori
    statistiche_cl.rename(index={"std":"Deviazione standard"}, inplace=True)
    statistiche_cl.rename(index={"mean":"Media"}, inplace=True)
    print(statistiche_cl)

#FUNZIONE CHE ELIMINA I DUPLICATI
def elimina_dupl(df):
  df=df.drop_duplicates()
  print(f"File con elementi non duplicati:\n {df}")  


#LISTA DI NOMI, ETA, CITTA E SALARIO
nome=["Pino", "Gino", "Sara", "Giulia", None]
eta=[10,20,30,90, np.nan]
citta=["Roma","Milano","Catanzaro","Napoli","Perugia", None]
salario=[10000,20000,30000,40000, np.nan]

#DIZIONARIO VUOTO
data={"nome":[],
      "eta":[],
      "citta":[],
      "salario":[]}

#ELIMINA RIGHE DOVE ALMENO UN ELEMENTO E' MANCANTE
def elimina_manc(df):
    df_cl=df.dropna()
    return df_cl

#inserimento nomi casuali
def crea_df():
    max=7
    #INSERIMENTO NOMI CASUALI
    for i in range(0,max):
        data["nome"].append(choice(nome))  
    #INSERIMENTO ETA CASUALE
    for i in range(0,max):
        data["eta"].append(choice(eta))
    #INSERIMENTO CITTA' CASUALI
    for i in range(0,max):
        data["citta"].append(choice(citta))
    #INSERIMENTO SALARI CASUALI
    for i in range(0,max):
        data["salario"].append(choice(salario))
#NSERIMENTO DI RIGHE DUPLICATE (PER DEBUG)
    data["nome"].append("Sara")
    data["eta"].append(10)
    data["citta"].append("Milano")
    data["salario"].append(10000)
    data["nome"].append("Sara")
    data["eta"].append(10)
    data["citta"].append("Milano")
    data["salario"].append(10000)
    df=pd.DataFrame(data)
    return df