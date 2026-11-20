import pandas as pd

data = pd.read_csv("../../qualite_air.csv")

print("Apercu des donnees :")
print(data.head())

print("\nDimensions (lignes, colonnes) :", data.shape)

print("\nInfos sur les colonnes :")
print(data.info())

print("\nStatistiques descriptives :")
print(data.describe())

print("\nValeurs manquantes :")
print(data.isnull().sum())

