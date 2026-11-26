import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("../Data/qualite_air.csv")
num_cols = df.select_dtypes(include="number").columns

if len(num_cols) >= 2:
    corr_matrix = df[num_cols].corr()
    print("Matrice de correlation :\n", corr_matrix)

    x = df[num_cols[0]]
    y = df[num_cols[1]]
    mask = x.notna() & y.notna()
    x, y = x[mask], y[mask]

    if len(x) > 1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        print(f"\nRegression lineaire ({num_cols[1]} en fonction de {num_cols[0]}) :")
        print(f"Pente (slope) : {slope:.4f}")
        print(f"Ordonnee a l'origine (intercept) : {intercept:.4f}")
        print(f"Coefficient de correlation r : {r_value:.4f}")
        print(f"p-value : {p_value:.4e}")
else:
    print("Pas assez de colonnes numeriques pour la correlation et la regression.")
