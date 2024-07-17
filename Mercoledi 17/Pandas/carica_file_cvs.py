import pandas as pd

# Percorso del file CSV
file_path = '5 settimana\\Mercoledi 17\\Pandas\\vendite.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare 
print(df.count("index"))