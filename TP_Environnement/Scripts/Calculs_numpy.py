import numpy as np
import pandas as pd

df = pd.read_csv("../Data/qualite_air.csv")
num_cols = df.select_dtypes(include="number").columns

for col in num_cols:
    arr = df[col].dropna().to_numpy()
    if len(arr) > 0:
        print(f"--- Variable : {col} ---")
        print("Moyenne :", np.mean(arr))
        print("Mediane :", np.median(arr))
        print("Ecart-type :", np.std(arr))
        print("Min / Max :", np.min(arr), "/", np.max(arr))
