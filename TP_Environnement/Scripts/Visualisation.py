import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Data/qualite_air.csv")

# Histogramme d'une variable numerique (ex: PM2.5 ou temperature)
num_cols = df.select_dtypes(include="number").columns
if len(num_cols) > 0:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[num_cols[0]].dropna(), kde=True)
    plt.title(f"Distribution de {num_cols[0]}")
    plt.tight_layout()
    plt.savefig("../Results/distribution.png")
    plt.close()

# Boxplot si au moins deux colonnes numeriques
if len(num_cols) > 1:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df[num_cols[:4]])
    plt.title("Boxplot des variables numeriques")
    plt.tight_layout()
    plt.savefig("../Results/boxplot.png")
    plt.close()

print("Graphiques enregistres dans ../Results/")
