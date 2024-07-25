"""
Partendo dal dataset a questo link 
https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression, 
utilizzate i dati sulle ore di studio e le ore di sonno per prevedere quanto 
queste caratteristiche influiscono sull'indice di prestazione degli studenti.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("6 settimana\\giovedi 25\\Student_Performance.csv")

print(df)
df.dropna()

df_train=df[["Hours Studied","Sleep Hours"]]
df_performance=df[["Performance Index"]]

print(df_train)
print(df_performance)


X_train, X_test, y_train,y_test=train_test_split(df_train,df_performance)

print(X_test.shape)
print(y_test.shape)


regr=LinearRegression().fit(df_train,df_performance)
#r_sw=coefficiente 
r_sq=regr.score(X_train, y_train)

print(r_sq)

print(f"intercept: {regr.intercept_}")

y_pred = regr.predict(X_test)
print(f"coefficients: {regr.coef_}")
plt.subplot(2,1,1)
plt.scatter(X_test["Hours Studied"],y_test, color="blue")
plt.plot(X_test["Hours Studied"],y_pred, color="green")
plt.subplot(2,1,2)
plt.scatter(X_test["Sleep Hours"],y_test, color="blue")
plt.plot(X_test["Sleep Hours"],y_pred, color="green")
plt.show()