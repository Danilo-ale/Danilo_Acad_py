import pandas as pd

df_v=pd.read_csv("5 settimana\\Giovedi 18\\vendite.csv")

df_c=pd.read_csv("5 settimana\\Giovedi 18\\costo_prod.csv")

print(df_v)
print(df_c)

df_p=df_v.merge(df_c)
print(df_p)
df_p["Totale vendite"]=df_p["Quantità"]*df_p["Costo per unità"]
pivot_df = df_p.pivot_table(values="Totale vendite", index="Prodotto", columns="Città", aggfunc="sum")
print(df_p)
print(pivot_df)
