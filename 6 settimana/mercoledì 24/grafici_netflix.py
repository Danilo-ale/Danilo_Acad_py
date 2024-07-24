"""
Sulla base del dataframe scaricato in precedenza con i dati Netflix:
- Grafico a Torta con le percentuali di prodotti Film o Serie TV;
- Grafico con la distribuzione dei prodotti per paese;
- Grafico con andamento dell'aggiunta dei prodotti nel corso del tempo.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("6 settimana\\netflix_titles.csv", index_col=0 ) 
print(df)
df.dropna(inplace=True)
conteggio=df["type"].value_counts()


perc_movie= (conteggio["Movie"]*100)/(conteggio["Movie"]+conteggio["TV Show"])
perc_movie=round(perc_movie,2)

perc_tvshow=(conteggio["TV Show"]*100)/(conteggio["Movie"]+conteggio["TV Show"])
perc_tvshow=round(perc_tvshow,2)

lista_programmi=[perc_tvshow, perc_movie]



def mappa_nazioni(country):
    if "," in country:
        naz_principale=country.split(",")[0]
        return naz_principale
    else:
        return country


#conteggio country

df["nazione_principale"] = df["country"].apply(mappa_nazioni)
print(df)
cont_country=df["nazione_principale"].value_counts()
#print(cont_country)

def mappa_data(date_added):
    date_added.replace(" ","")
    anno=date_added.split(",")[1]
    return anno


df["data_aggiunta"] = df["date_added"].apply(mappa_data)
df["data_aggiunta"] = df["data_aggiunta"].astype(int)

cont_anno=df["data_aggiunta"].value_counts().sort_index()
print(cont_anno)
#Andamento dei Contenuti Netflix aggiunti nel tempo
plt.figure()
cont_anno.plot(kind="line", color='blue')
plt.title('Andamento dei Contenuti Netflix aggiunti nel tempo')
plt.xlabel('Anno')
plt.ylabel('Numero di Titoli')
plt.show()

#Distribuzione dei Contenuti Netflix per Paese
plt.figure()
cont_country.plot(kind='bar', color='#ff9999')
plt.title('Distribuzione dei Contenuti Netflix per Paese')
plt.xlabel('Paese')
plt.ylabel('Numero di Titoli')
plt.show()

#Grafico a torta
plt.figure()
plt.pie(lista_programmi, labels=["TV Show","Movie"])
plt.show()