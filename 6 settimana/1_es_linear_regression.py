"""
Utilizzate la linear regression per analizzare il dataframe
 di esempio in cui abbiamo le Calorie bruciate in base 
 al peso della persona che fa esercizio fisico con la montain bike, 
 allenate l'algoritmo, testatelo e poi realizzate un grafico
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df=pd.read_csv("6 settimana\\giovedi 25\\calories.csv")
print(df)
df = df.drop(df.columns[0], axis=1)
print(df)
df_kg=df["kg"]
df_kg_array = df_kg.values[:, np.newaxis]
df_cal=df["calories"]
#X_train, X_test, y_train, y_test = train_test_split(df["kg"], df["calories"])
X_train=df_kg_array[:-20]
X_test=df_kg_array[-20:]
y_train=df_cal[:-20]
y_test=df_cal[-20:]
#X_train=X_train.reshape((-1, 1))

regr = linear_model.LinearRegression()
regr.fit(X_train,y_train)
y_pred=regr.predict(X_test)
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)

plt.show()