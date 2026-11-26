import pandas as pd

print("==========================================")
print("ANALYSE QUALITE DE L'AIR - PARTIE A")
print("==========================================")

try:
    df = pd.read_csv("../Data/qualite_air.csv")
    print("Apercu des donnees :")
    print(df.head())
    print("\nInformations generales :")
    print(df.info())
    print("\nStatistiques descriptives :")
    print(df.describe())
except FileNotFoundError:
    print("Fichier ../Data/qualite_air.csv introuvable pour le moment.")
