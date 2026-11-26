import pandas as pd

df = pd.read_csv("../Data/qualite_air.csv")

print("Dimensions (lignes, colonnes) :", df.shape)
print("\nTypes de donnees :\n", df.dtypes)
print("\nValeurs manquantes :\n", df.isnull().sum())
print("\nPremieres lignes :\n", df.head())
print("\nResume statistique :\n", df.describe())
